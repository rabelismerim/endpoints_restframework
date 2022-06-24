from django.db import models
from polls.mestre.models import mestre
from polls.aluno.models import aluno

class mestrealuno(models.Model):

    id_mestre = models.ForeignKey(mestre, on_delete=models.PROTECT)
    txt_ano_fiscal = models.CharField(max_length=50, blank=True, verbose_name="Ano Fiscal")
    dt_criacao = models.DateField(null=True, blank=True, verbose_name='Data de Criação')
    id_aluno = models.ForeignKey(aluno, on_delete=models.PROTECT)
    
                            
    class Meta:
           verbose_name='mestre_aluno'
           verbose_name_plural='mestre_aluno'
    
    def __str__(self):
        return self.txt_ano_fiscal

