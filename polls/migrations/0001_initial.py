# Generated by Django 4.0.5 on 2022-06-09 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt_name', models.CharField(blank=True, max_length=200, verbose_name='Nome')),
                ('txt_time', models.CharField(blank=True, max_length=50, verbose_name='Time')),
                ('txt_email', models.CharField(blank=True, max_length=50, verbose_name='E-mail')),
                ('bl_usuario_ativo', models.BooleanField(blank=True, null=True, verbose_name='Usuário Ativo?')),
                ('dt_criacao', models.DateField(blank=True, null=True, verbose_name='Data de Criação')),
                ('dt_atualizacao', models.DateField(blank=True, null=True, verbose_name='Data de Atualização')),
            ],
            options={
                'verbose_name': 'coach',
                'verbose_name_plural': 'coach',
            },
        ),
        migrations.CreateModel(
            name='coach_coachee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt_ano_fiscal', models.CharField(blank=True, max_length=50, verbose_name='Ano Fiscal')),
                ('dt_criacao', models.DateField(blank=True, null=True, verbose_name='Data de Criação')),
                ('id_coach', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.coach')),
            ],
            options={
                'verbose_name': 'coach_coachee',
                'verbose_name_plural': 'coach_coachee',
            },
        ),
        migrations.CreateModel(
            name='competencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt_cargo', models.CharField(blank=True, max_length=50, verbose_name='Cargo')),
                ('txt_tipo', models.CharField(blank=True, max_length=50, verbose_name='Tipo')),
                ('txt_competencia', models.CharField(blank=True, max_length=50, verbose_name='Competencia')),
                ('dt_criacao', models.DateField(blank=True, null=True, verbose_name='Data de Criação')),
                ('dt_atualizacao', models.DateField(blank=True, null=True, verbose_name='Data de Atualização')),
            ],
            options={
                'verbose_name': 'competencia',
                'verbose_name_plural': 'competencia',
            },
        ),
        migrations.CreateModel(
            name='reuniao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt_comentario', models.CharField(blank=True, max_length=200, verbose_name='Comentario')),
                ('dt_criacao', models.DateField(blank=True, null=True, verbose_name='Data de Criação')),
                ('dt_atualizacao', models.DateField(blank=True, null=True, verbose_name='Data de Atualização')),
                ('id_coach_coachee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.coach_coachee')),
            ],
        ),
        migrations.CreateModel(
            name='reuniao_tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt_atividade', models.CharField(blank=True, max_length=50, verbose_name='Atividade')),
                ('txt_status', models.CharField(choices=[('0', 'Pendente'), ('1', 'Em andamento'), ('2', 'Concluído')], default='0', max_length=1)),
                ('dt_conclusao', models.DateField(blank=True, null=True, verbose_name='Data de Conclusão')),
                ('nr_prazo', models.IntegerField(blank=True, null=True, verbose_name='Prazo')),
                ('txt_observacao', models.TextField(blank=True, max_length=200, verbose_name='Observação')),
                ('dt_criacao', models.DateField(auto_now_add=True, null=True, verbose_name='Data de Criação')),
                ('dt_atualizacao', models.DateField(auto_now=True, null=True, verbose_name='Data de Atualização')),
                ('id_competencia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.competencia')),
                ('id_reuniao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.reuniao')),
            ],
        ),
        migrations.CreateModel(
            name='coachee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt_name', models.CharField(blank=True, max_length=200, verbose_name='  Nome')),
                ('txt_time', models.CharField(blank=True, max_length=50, verbose_name='Time')),
                ('txt_email', models.CharField(blank=True, max_length=50, verbose_name='E-mail')),
                ('txt_categoria_cargo', models.CharField(blank=True, max_length=50, verbose_name='Categoria Cargo')),
                ('txt_cargo', models.CharField(blank=True, max_length=50, verbose_name='Cargo')),
                ('txt_area', models.CharField(blank=True, max_length=50, verbose_name='Area')),
                ('txt_linha_servico', models.CharField(blank=True, max_length=50, verbose_name='Linha de Serviço')),
                ('txt_nivel_ingles', models.CharField(blank=True, max_length=50, verbose_name='Nivel de Inglês')),
                ('txt_business_chemistry', models.CharField(blank=True, max_length=50, verbose_name='Business Chemistry')),
                ('bl_usuario_ativo', models.BooleanField(blank=True, null=True, verbose_name='Usuário Ativo?')),
                ('dt_criacao', models.DateField(blank=True, null=True, verbose_name='Data de Criação')),
                ('dt_atualizacao', models.DateField(blank=True, null=True, verbose_name='Data de Atualização')),
                ('id_coach', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.coach')),
                ('id_competencia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.competencia')),
            ],
            options={
                'verbose_name': 'coachee',
                'verbose_name_plural': 'coachee',
            },
        ),
        migrations.AddField(
            model_name='coach_coachee',
            name='id_coachee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.coachee'),
        ),
    ]
