"""Preserva permissões atribuídas a usuários e grupos antes da renomeação."""
from django.db import migrations

RENAMES = (("coach", "mestre"), ("coachee", "aluno"),
           ("coach_coachee", "mestrealuno"), ("reuniao_tarefa", "reuniaotarefa"))


def forwards(apps, schema_editor):
    Permission = apps.get_model("auth", "Permission")
    for old, new in RENAMES:
        for action in ("add", "change", "delete", "view"):
            Permission.objects.using(schema_editor.connection.alias).filter(
                content_type__app_label="polls", content_type__model=new, codename=f"{action}_{old}",
            ).update(codename=f"{action}_{new}", name=f"Can {action} {new}")


def backwards(apps, schema_editor):
    # A reversão ocorre antes de RenameModel restaurar os content types.
    Permission = apps.get_model("auth", "Permission")
    for old, new in RENAMES:
        for action in ("add", "change", "delete", "view"):
            Permission.objects.using(schema_editor.connection.alias).filter(
                content_type__app_label="polls", content_type__model=new, codename=f"{action}_{new}",
            ).update(codename=f"{action}_{old}", name=f"Can {action} {old}")


class Migration(migrations.Migration):
    dependencies = [
        ("polls", "0003_alter_aluno_options_alter_competencia_options_and_more"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("contenttypes", "0002_remove_content_type_name"),
    ]
    operations = [migrations.RunPython(forwards, backwards)]
