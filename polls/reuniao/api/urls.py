from django.urls import path
from .views import ReuniaoDetailView, ReuniaoListCreate


urlpatterns = [

path('reuniao/', ReuniaoListCreate.as_view(), name="reuniao-list"),
path('reuniao/<int:pk>', ReuniaoDetailView.as_view(), name="reuniao-detail")      

]