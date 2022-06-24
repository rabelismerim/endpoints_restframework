from django.urls import path
from .views import MestreDetailView, MestreListCreate

urlpatterns = [
    path('mestre/', MestreListCreate.as_view(), name="mestre-list"),
    path('mestre/<int:pk>', MestreDetailView.as_view(), name="mestre-detail")
]