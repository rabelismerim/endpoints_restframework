from rest_framework import generics
from polls.competencia.models import competencia
from polls.reuniao.models import reuniao
from polls.reuniao_tarefa.models import reuniao_tarefa
from .serializers import ReuniaotarefaSerializer
from rest_framework.generics import get_object_or_404


class ReuniaotarefaListCreate(generics.ListCreateAPIView):

    queryset = reuniao_tarefa.objects.all().order_by('-id')
    serializer_class = ReuniaotarefaSerializer
    #permission_classes = [DjangoModelPermissions] - define que nessa view aplica os permissionamentos definidos no admin



class ReuniaotarefaDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = reuniao_tarefa.objects.all().order_by('-id')
    serializer_class = ReuniaotarefaSerializer