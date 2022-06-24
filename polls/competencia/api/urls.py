from django.urls import path
from .views import CompetenciaDetailView, CompetenciaListCreate

urlpatterns = [
path('competencia/', CompetenciaListCreate.as_view(), name="competencia-list"),
path('competencia/<int:pk>', CompetenciaDetailView.as_view(), name="competencia-detail")    
  

]