from django.urls import path
from .views import ReuniaotarefaDetailView, ReuniaotarefaListCreate


urlpatterns = [

path('reuniao_tarefa/', ReuniaotarefaListCreate.as_view(), name="reuniao_tarefa-list"),
path('reuniao_tarefa/<int:pk>', ReuniaotarefaDetailView.as_view(), name="reuniao_tarefa-detail")      

]
    

