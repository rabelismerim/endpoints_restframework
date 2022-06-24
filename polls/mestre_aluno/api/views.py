from rest_framework import generics
from polls.mestre_aluno.models import mestrealuno
from .serializers import MestrealunoSerializer
from rest_framework.generics import get_object_or_404


class MestrealunoListCreate(generics.ListCreateAPIView):

    queryset = mestrealuno.objects.all().order_by('-id')
    serializer_class = MestrealunoSerializer
    

class MestrealunoDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = mestrealuno.objects.all().order_by('-id')
    serializer_class = MestrealunoSerializer