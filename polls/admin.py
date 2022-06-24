from django.contrib import admin

from polls.mestre.models import mestre
from polls.aluno.models import aluno
from polls.mestre_aluno.models import mestrealuno
from polls.reuniao.models import reuniao
from polls.reuniao_tarefa.models import reuniao_tarefa
from polls.competencia.models import competencia

admin.site.register(mestre),
admin.site.register(aluno),
admin.site.register(mestrealuno),
admin.site.register(reuniao),
admin.site.register(reuniao_tarefa)
admin.site.register(competencia)
# Register your models here.
