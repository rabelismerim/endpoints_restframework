"""Domínio de mentoria. Uma aplicação Django e um histórico de migrações."""
from django.db import models


class Mestre(models.Model):
    txt_name = models.CharField("Nome", max_length=200, blank=True)
    txt_time = models.CharField("Time", max_length=50, blank=True)
    txt_email = models.CharField("E-mail", max_length=50, blank=True)
    bl_usuario_ativo = models.BooleanField("Usuário ativo?", null=True, blank=True)
    dt_criacao = models.DateField("Data de criação", null=True, blank=True)
    dt_atualizacao = models.DateField("Data de atualização", null=True, blank=True)

    class Meta:
        verbose_name = "mestre"
        verbose_name_plural = "mestres"

    def __str__(self):
        return self.txt_name or f"Mestre #{self.pk}"


class Competencia(models.Model):
    txt_cargo = models.CharField("Cargo", max_length=50, blank=True)
    txt_tipo = models.CharField("Tipo", max_length=50, blank=True)
    txt_competencia = models.CharField("Competência", max_length=50, blank=True)
    dt_criacao = models.DateField("Data de criação", null=True, blank=True)
    dt_atualizacao = models.DateField("Data de atualização", null=True, blank=True)

    class Meta:
        verbose_name = "competência"
        verbose_name_plural = "competências"

    def __str__(self):
        return self.txt_competencia or f"Competência #{self.pk}"


class Aluno(models.Model):
    id_competencia = models.ForeignKey(Competencia, on_delete=models.PROTECT)
    id_mestre = models.ForeignKey(Mestre, on_delete=models.PROTECT)
    txt_name = models.CharField("Nome", max_length=200, blank=True)
    txt_time = models.CharField("Time", max_length=50, blank=True)
    txt_email = models.CharField("E-mail", max_length=50, blank=True)
    txt_categoria_cargo = models.CharField("Categoria do cargo", max_length=50, blank=True)
    txt_cargo = models.CharField("Cargo", max_length=50, blank=True)
    txt_area = models.CharField("Área", max_length=50, blank=True)
    txt_linha_servico = models.CharField("Linha de serviço", max_length=50, blank=True)
    txt_nivel_ingles = models.CharField("Nível de inglês", max_length=50, blank=True)
    txt_business_chemistry = models.CharField("Business Chemistry", max_length=50, blank=True)
    bl_usuario_ativo = models.BooleanField("Usuário ativo?", null=True, blank=True)
    dt_criacao = models.DateField("Data de criação", null=True, blank=True)
    dt_atualizacao = models.DateField("Data de atualização", null=True, blank=True)

    class Meta:
        verbose_name = "aluno"
        verbose_name_plural = "alunos"

    def __str__(self):
        return self.txt_name or f"Aluno #{self.pk}"


class MestreAluno(models.Model):
    id_mestre = models.ForeignKey(Mestre, on_delete=models.PROTECT)
    id_aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    txt_ano_fiscal = models.CharField("Ano fiscal", max_length=50, blank=True)
    dt_criacao = models.DateField("Data de criação", null=True, blank=True)

    class Meta:
        verbose_name = "vínculo de mentoria"
        verbose_name_plural = "vínculos de mentoria"

    def __str__(self):
        return f"{self.id_mestre} → {self.id_aluno} ({self.txt_ano_fiscal})"


class Reuniao(models.Model):
    txt_comentario = models.CharField("Comentário", max_length=200, blank=True)
    dt_criacao = models.DateField("Data de criação", null=True, blank=True)
    dt_atualizacao = models.DateField("Data de atualização", null=True, blank=True)
    id_mestre_aluno = models.ForeignKey(MestreAluno, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "reunião"
        verbose_name_plural = "reuniões"

    def __str__(self):
        return self.txt_comentario or f"Reunião #{self.pk}"


class ReuniaoTarefa(models.Model):
    class Status(models.TextChoices):
        PENDENTE = "0", "Pendente"
        EM_ANDAMENTO = "1", "Em andamento"
        CONCLUIDO = "2", "Concluído"

    txt_atividade = models.CharField("Atividade", max_length=50, blank=True)
    txt_status = models.CharField(max_length=1, choices=Status.choices, default=Status.PENDENTE)
    dt_conclusao = models.DateField("Data de conclusão", null=True, blank=True)
    nr_prazo = models.IntegerField("Prazo (dias)", null=True, blank=True)
    txt_observacao = models.TextField("Observação", max_length=200, blank=True)
    dt_criacao = models.DateField("Data de criação", null=True, blank=True, auto_now_add=True)
    dt_atualizacao = models.DateField("Data de atualização", null=True, blank=True, auto_now=True)
    id_reuniao = models.ForeignKey(Reuniao, on_delete=models.PROTECT)
    id_competencia = models.ForeignKey(Competencia, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "tarefa de reunião"
        verbose_name_plural = "tarefas de reunião"

    def __str__(self):
        return self.txt_atividade or f"Tarefa #{self.pk}"
