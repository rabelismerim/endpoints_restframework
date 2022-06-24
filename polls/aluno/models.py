from django.db import models
from polls.competencia.models import competencia
from polls.mestre.models import mestre
class aluno(models.Model):
     id_competencia = models.ForeignKey(competencia, on_delete=models.PROTECT)
     txt_name = models.CharField(max_length=200, blank=True, verbose_name="  Nome")
     txt_time = models.CharField(max_length=50, blank=True, verbose_name="Time")
     txt_email = models.CharField(max_length=50, blank=True, verbose_name="E-mail")
     txt_categoria_cargo = models.CharField(max_length=50, blank=True, verbose_name="Categoria Cargo")
     txt_cargo = models.CharField(max_length=50, blank=True, verbose_name="Cargo")
     txt_area = models.CharField(max_length=50, blank=True, verbose_name="Area")
     txt_linha_servico = models.CharField(max_length=50, blank=True, verbose_name="Linha de Serviço")
     txt_nivel_ingles = models.CharField(max_length=50, blank=True, verbose_name="Nivel de Inglês")
     txt_business_chemistry = models.CharField(max_length=50, blank=True, verbose_name="Business Chemistry")
     bl_usuario_ativo = models.BooleanField(null=True, blank=True, verbose_name='Usuário Ativo?')
     dt_criacao = models.DateField(null=True, blank=True, verbose_name='Data de Criação')
     dt_atualizacao = models.DateField(null=True, blank=True, verbose_name='Data de Atualização')
     id_mestre = models.ForeignKey(mestre, on_delete=models.PROTECT)
    
     class Meta:
         verbose_name='aluno'
         verbose_name_plural='aluno'

     def __str__(self):
        return self.txt_name

