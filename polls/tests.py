from io import StringIO

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.core.management import call_command
from django.db import connection
from django.db.migrations.executor import MigrationExecutor
from django.test import TransactionTestCase
from rest_framework.test import APITestCase
from .models import Aluno, Competencia, Mestre, MestreAluno, Reuniao, ReuniaoTarefa


class MentoriaAPITests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser("admin", "admin@example.com", "test-password")
        self.mestre = Mestre.objects.create(txt_name="Ana", txt_email="ana@example.com")
        self.competencia = Competencia.objects.create(txt_competencia="Comunicação")
        self.aluno = Aluno.objects.create(txt_name="Bruno", id_mestre=self.mestre, id_competencia=self.competencia)
        self.vinculo = MestreAluno.objects.create(id_mestre=self.mestre, id_aluno=self.aluno, txt_ano_fiscal="2026")
        self.reuniao = Reuniao.objects.create(txt_comentario="Planejamento", id_mestre_aluno=self.vinculo)

    def test_anonymous_read_and_write_permissions(self):
        for resource in ("mestre", "aluno", "competencia", "mestre_aluno", "reuniao", "reuniao_tarefa"):
            with self.subTest(resource=resource):
                url = f"/api/polls/{resource}/"
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                self.assertIsInstance(response.data, list)
                self.assertEqual(self.client.post(url, {}, format="json").status_code, 403)
        self.assertEqual(self.client.patch(f"/api/polls/mestre/{self.mestre.pk}", {"txt_name": "Outro"}).status_code, 403)
        self.assertEqual(self.client.delete(f"/api/polls/mestre/{self.mestre.pk}").status_code, 403)

    def test_model_permissions_for_regular_user(self):
        user = get_user_model().objects.create_user("editor", password="test-password")
        self.client.force_authenticate(user)
        url = "/api/polls/mestre/"
        self.assertEqual(self.client.post(url, {"txt_name": "Editor"}).status_code, 403)
        user.user_permissions.add(Permission.objects.get(codename="add_mestre", content_type__app_label="polls"))
        # Recarrega para limpar o cache de permissões do usuário.
        self.client.force_authenticate(get_user_model().objects.get(pk=user.pk))
        response = self.client.post(url, {"txt_name": "Editor"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.client.delete(f"{url}{response.data['id']}/").status_code, 403)

    def test_crud_for_all_resources_and_legacy_details(self):
        self.client.force_authenticate(self.user)
        cases = (
            ("mestre", {"txt_name": "Carla", "txt_email": "carla@example.com"}, "txt_name"),
            ("aluno", {"txt_name": "Diego", "id_mestre": self.mestre.pk, "id_competencia": self.competencia.pk}, "txt_name"),
            ("competencia", {"txt_competencia": "Liderança"}, "txt_competencia"),
            ("mestre_aluno", {"id_mestre": self.mestre.pk, "id_aluno": self.aluno.pk, "txt_ano_fiscal": "2027"}, "txt_ano_fiscal"),
            ("reuniao", {"id_mestre_aluno": self.vinculo.pk, "txt_comentario": "Feedback"}, "txt_comentario"),
            ("reuniao_tarefa", {"id_reuniao": self.reuniao.pk, "id_competencia": self.competencia.pk, "txt_atividade": "Curso"}, "txt_atividade"),
        )
        for resource, payload, field in cases:
            with self.subTest(resource=resource):
                url = f"/api/polls/{resource}/"
                created = self.client.post(url, payload, format="json")
                self.assertEqual(created.status_code, 201, created.data)
                detail = f"{url}{created.data['id']}"
                self.assertEqual(self.client.get(detail).status_code, 200)
                self.assertEqual(self.client.get(detail + "/").status_code, 200)
                self.assertEqual(self.client.put(detail, payload, format="json").status_code, 200)
                patched = self.client.patch(detail, {field: "Atualizado"}, format="json")
                self.assertEqual(patched.status_code, 200)
                self.assertEqual(patched.data[field], "Atualizado")
                self.assertEqual(self.client.delete(detail).status_code, 204)
                self.assertEqual(self.client.get(detail).status_code, 404)

    def test_validation(self):
        self.client.force_authenticate(self.user)
        self.assertEqual(self.client.post("/api/polls/mestre/", {"txt_email": "invalido"}).status_code, 400)
        self.assertEqual(self.client.post("/api/polls/aluno/", {"id_mestre": 999999, "id_competencia": self.competencia.pk}).status_code, 400)
        url = "/api/polls/reuniao_tarefa/"
        payload = {"id_reuniao": self.reuniao.pk, "id_competencia": self.competencia.pk}
        for invalid in ({"nr_prazo": -1}, {"txt_status": "9"}):
            self.assertEqual(self.client.post(url, {**payload, **invalid}, format="json").status_code, 400)
        created = self.client.post(url, {**payload, "dt_criacao": "2000-01-01"}, format="json")
        self.assertEqual(created.status_code, 201)
        self.assertNotEqual(created.data["dt_criacao"], "2000-01-01")

    def test_protected_delete_is_conflict(self):
        self.client.force_authenticate(self.user)
        for resource, instance in (("mestre", self.mestre), ("aluno", self.aluno), ("competencia", self.competencia), ("mestre_aluno", self.vinculo)):
            response = self.client.delete(f"/api/polls/{resource}/{instance.pk}/")
            self.assertEqual(response.status_code, 409)
            self.assertIn("detail", response.data)
            self.assertTrue(type(instance).objects.filter(pk=instance.pk).exists())

    def test_search_ordering_and_api_root(self):
        Mestre.objects.create(txt_name="Zélia")
        response = self.client.get("/api/polls/mestre/?search=Ana")
        self.assertEqual([item["id"] for item in response.data], [self.mestre.pk])
        response = self.client.get("/api/polls/mestre/?ordering=id")
        self.assertEqual(response.data[0]["id"], self.mestre.pk)
        root = self.client.get("/api/polls/")
        self.assertEqual(root.status_code, 200)
        self.assertEqual(len(root.data), 6)
        self.assertRedirects(self.client.get("/"), "/api/polls/", fetch_redirect_response=False)


class DemoDataTests(APITestCase):
    def test_seed_demo_is_idempotent(self):
        models = (Mestre, Aluno, Competencia, MestreAluno, Reuniao, ReuniaoTarefa)
        call_command("seed_demo", stdout=StringIO())
        before = [model.objects.count() for model in models]
        call_command("seed_demo", stdout=StringIO())
        self.assertEqual(before, [1] * 6)
        self.assertEqual(before, [model.objects.count() for model in models])


class LegacyMigrationTests(TransactionTestCase):
    def test_records_relationships_and_permissions_survive_upgrade(self):
        try:
            call_command("migrate", "polls", "0001", verbosity=0, stdout=StringIO())
            old = MigrationExecutor(connection).loader.project_state([("polls", "0001_initial")]).apps
            coach = old.get_model("polls", "coach").objects.create(txt_name="Legado", txt_email="legacy@example.com")
            skill = old.get_model("polls", "competencia").objects.create(txt_competencia="Legado")
            coachee = old.get_model("polls", "coachee").objects.create(txt_name="Aluno legado", id_coach_id=coach.pk, id_competencia_id=skill.pk)
            link = old.get_model("polls", "coach_coachee").objects.create(id_coach_id=coach.pk, id_coachee_id=coachee.pk)
            meeting = old.get_model("polls", "reuniao").objects.create(id_coach_coachee_id=link.pk)
            task = old.get_model("polls", "reuniao_tarefa").objects.create(id_reuniao_id=meeting.pk, id_competencia_id=skill.pk, txt_atividade="Preservar")
            user = get_user_model().objects.create_user("legacy")
            permission = Permission.objects.get(content_type__app_label="polls", codename="add_coach")
            permission_id = permission.pk
            user.user_permissions.add(permission)
            call_command("migrate", "polls", verbosity=0, stdout=StringIO())
            self.assertEqual(Mestre.objects.get(pk=coach.pk).txt_name, "Legado")
            self.assertEqual(Aluno.objects.get(pk=coachee.pk).id_mestre_id, coach.pk)
            self.assertEqual(MestreAluno.objects.get(pk=link.pk).id_aluno_id, coachee.pk)
            self.assertEqual(Reuniao.objects.get(pk=meeting.pk).id_mestre_aluno_id, link.pk)
            self.assertEqual(ReuniaoTarefa.objects.get(pk=task.pk).txt_atividade, "Preservar")
            self.assertEqual(Competencia.objects.get(pk=skill.pk).txt_competencia, "Legado")
            self.assertEqual(Permission.objects.get(pk=permission_id).codename, "add_mestre")
            self.assertTrue(get_user_model().objects.get(pk=user.pk).has_perm("polls.add_mestre"))
        finally:
            call_command("migrate", "polls", verbosity=0, stdout=StringIO())
