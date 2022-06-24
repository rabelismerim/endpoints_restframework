from django.urls import path
from .views import AlunoDetailView, AlunoListCreate

urlpatterns = [

 path('aluno/', AlunoListCreate.as_view(), name="aluno-list"),
 path('aluno/<int:pk>', AlunoDetailView.as_view(), name="aluno-detail")    

]