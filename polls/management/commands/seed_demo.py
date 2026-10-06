"""Cria somente dados fictícios; não cria usuários nem altera registros existentes."""
from django.core.management.base import BaseCommand
from django.db import transaction
from polls.models import Aluno, Competencia, Mestre, MestreAluno, Reuniao, ReuniaoTarefa


class Command(BaseCommand):
    help = "Cria dados fictícios de mentoria para explorar a API localmente."

    @transaction.atomic
    def handle(self, *args, **options):
        competencia, _ = Competencia.objects.get_or_create(
            txt_competencia="Comunicação — demonstração",
            defaults={"txt_tipo": "Comportamental", "txt_cargo": "Analista"},
        )
        mestre, _ = Mestre.objects.get_or_create(
            txt_email="ana.demo@example.com",
            defaults={"txt_name": "Ana Martins (demo)", "txt_time": "Desenvolvimento", "bl_usuario_ativo": True},
        )
        aluno, _ = Aluno.objects.get_or_create(
            txt_email="bruno.demo@example.com",
            defaults={"txt_name": "Bruno Lima (demo)", "txt_time": "Desenvolvimento", "txt_cargo": "Analista",
                      "bl_usuario_ativo": True, "id_mestre": mestre, "id_competencia": competencia},
        )
        vinculo, _ = MestreAluno.objects.get_or_create(id_mestre=mestre, id_aluno=aluno, txt_ano_fiscal="2026")
        reuniao, _ = Reuniao.objects.get_or_create(
            id_mestre_aluno=vinculo, txt_comentario="Definição do plano de desenvolvimento (demo)",
        )
        ReuniaoTarefa.objects.get_or_create(
            id_reuniao=reuniao, id_competencia=competencia, txt_atividade="Preparar apresentação (demo)",
            defaults={"nr_prazo": 7, "txt_status": ReuniaoTarefa.Status.EM_ANDAMENTO},
        )
        self.stdout.write(self.style.SUCCESS("Dados fictícios disponíveis. Execute novamente sem duplicá-los."))
