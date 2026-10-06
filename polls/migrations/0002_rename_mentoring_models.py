"""Renomeia as entidades legadas sem recriar ou apagar registros."""
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("polls", "0001_initial")]
    operations = [
        migrations.RenameModel("coach_coachee", "MestreAluno"),
        migrations.RenameModel("coachee", "Aluno"),
        migrations.RenameModel("coach", "Mestre"),
        migrations.RenameModel("reuniao_tarefa", "ReuniaoTarefa"),
        migrations.RenameField("aluno", "id_coach", "id_mestre"),
        migrations.RenameField("mestrealuno", "id_coach", "id_mestre"),
        migrations.RenameField("mestrealuno", "id_coachee", "id_aluno"),
        migrations.RenameField("reuniao", "id_coach_coachee", "id_mestre_aluno"),
    ]
