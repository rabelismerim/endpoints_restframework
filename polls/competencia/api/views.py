from rest_framework import generics
from polls.competencia.models import competencia
from polls.reuniao.models import reuniao
from .serializers import CompetenciaSerializer
from rest_framework.generics import get_object_or_404


class CompetenciaListCreate(generics.ListCreateAPIView):

    queryset = competencia.objects.all().order_by('-id')
    serializer_class = CompetenciaSerializer
        

class CompetenciaDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = competencia.objects.all().order_by('-id')
    serializer_class = CompetenciaSerializer