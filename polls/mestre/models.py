from django.db import models

class mestre(models.Model):

    txt_name = models.CharField(max_length=200, blank=True, verbose_name="Nome")
    txt_time = models.CharField(max_length=50, blank=True, verbose_name="Time")
    txt_email = models.CharField(max_length=50, blank=True, verbose_name="E-mail")
    bl_usuario_ativo = models.BooleanField(null=True, blank=True, verbose_name='Usuário Ativo?')
    dt_criacao = models.DateField(null=True, blank=True, verbose_name='Data de Criação')
    dt_atualizacao = models.DateField(null=True, blank=True, verbose_name='Data de Atualização')

    
    class Meta:
        verbose_name='mestre'
        verbose_name_plural='mestre'

    def __str__(self):
        return self.txt_name
