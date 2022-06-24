from django.db import models

class competencia(models.Model):

    txt_cargo = models.CharField(max_length=50, blank=True, verbose_name="Cargo")
    txt_tipo = models.CharField(max_length=50, blank=True, verbose_name="Tipo")
    txt_competencia = models.CharField(max_length=50, blank=True, verbose_name="Competencia")
    dt_criacao = models.DateField(null=True, blank=True, verbose_name='Data de Criação')
    dt_atualizacao = models.DateField(null=True, blank=True, verbose_name='Data de Atualização')
    
                            
    class Meta:
           verbose_name='competencia'
           verbose_name_plural='competencia'
 
    def __str__(self):
        return self.txt_competencia
