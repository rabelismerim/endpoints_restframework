from rest_framework import generics
from polls.mestre.models import mestre
from .serializers import MestreSerializer
from rest_framework.generics import get_object_or_404



class MestreListCreate(generics.ListCreateAPIView):

    queryset = mestre.objects.all().order_by('-id')
    serializer_class = MestreSerializer
    

class MestreDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = mestre.objects.all().order_by('-id')
    serializer_class = MestreSerializer