from rest_framework import generics
from polls.aluno.models import aluno
from .serializers import AlunoSerializer
from rest_framework.generics import get_object_or_404
from polls.mestre.models import mestre

class AlunoListCreate(generics.ListCreateAPIView):

    queryset = aluno.objects.all().order_by('-id')
    serializer_class = AlunoSerializer
       

class AlunoDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = aluno.objects.all().order_by('-id')
    serializer_class = AlunoSerializer