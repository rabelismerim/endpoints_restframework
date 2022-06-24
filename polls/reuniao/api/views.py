from rest_framework import generics
from polls.competencia.models import competencia
from polls.reuniao.models import reuniao
from .serializers import ReuniaoSerializer
from rest_framework.generics import get_object_or_404


class ReuniaoListCreate(generics.ListCreateAPIView):

    queryset = reuniao.objects.all().order_by('-id')
    serializer_class = ReuniaoSerializer
    

class ReuniaoDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = reuniao.objects.all().order_by('-id')
    serializer_class = ReuniaoSerializer