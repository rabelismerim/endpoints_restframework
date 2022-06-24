from django.db import models
from polls.reuniao.models import reuniao
from polls.competencia.models import competencia

class reuniao_tarefa(models.Model):

    STATUS_CHOICES = (
        ("0","Pendente"),
        ("1","Em andamento"),
        ("2","Concluído")
    )
    txt_atividade = models.CharField(max_length=50, blank=True, verbose_name="Atividade")
    txt_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0')
    dt_conclusao = models.DateField(null=True, blank=True, verbose_name='Data de Conclusão')
    nr_prazo = models.IntegerField(null=True, blank=True, verbose_name='Prazo')
    txt_observacao = models.TextField(max_length=200, blank=True, verbose_name="Observação")
    dt_criacao = models.DateField(null=True, blank=True, auto_now_add=True, verbose_name='Data de Criação')
    dt_atualizacao = models.DateField(null=True, blank=True, auto_now=True, verbose_name='Data de Atualização')
    id_reuniao = models.ForeignKey(reuniao, on_delete=models.PROTECT)
    id_competencia = models.ForeignKey(competencia, on_delete=models.PROTECT)
 
class Meta:
     verbose_name='reuniao_tarefa'
     verbose_name_plural='reuniao_tarefa'

def __str__(self):
         return self.txt_atividade

