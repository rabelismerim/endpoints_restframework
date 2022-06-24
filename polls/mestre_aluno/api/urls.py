from django.urls import path
from .views import MestrealunoDetailView, MestrealunoListCreate


urlpatterns = [

path('mestre_aluno/', MestrealunoListCreate.as_view(), name="mestre_aluno-list"),
path('mestre_aluno/<int:pk>', MestrealunoDetailView.as_view(), name="mestre_aluno-detail")    

]