from django.db import models
from polls.mestre_aluno.models import mestrealuno

class reuniao(models.Model):
 
    txt_comentario = models.CharField(max_length=200, blank=True, verbose_name="Comentario")
    dt_criacao = models.DateField(null=True, blank=True, verbose_name='Data de Criação')
    dt_atualizacao = models.DateField(null=True, blank=True, verbose_name='Data de Atualização')
    id_mestre_aluno = models.ForeignKey(mestrealuno, on_delete=models.PROTECT)
     
    class Meta:
        verbose_name='reuniao'
        verbose_name_plural='reuniao'

    def __str__(self):
            return self.txt_comentario


