from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    AlunoViewSet, CompetenciaViewSet, MestreViewSet, MestreAlunoViewSet, ReuniaoViewSet, ReuniaoTarefaViewSet,
)

router = DefaultRouter()
resources = (
    ("mestre", MestreViewSet), ("aluno", AlunoViewSet), ("competencia", CompetenciaViewSet),
    ("mestre_aluno", MestreAlunoViewSet), ("reuniao", ReuniaoViewSet), ("reuniao_tarefa", ReuniaoTarefaViewSet),
)
for prefix, viewset in resources:
    router.register(prefix, viewset, basename=prefix)

# Mantém os detalhes antigos sem barra final, incluindo PUT/PATCH/DELETE.
urlpatterns = [
    path(f"{prefix}/<int:pk>", viewset.as_view({
        "get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy",
    }), name=f"{prefix}-detail-legacy") for prefix, viewset in resources
] + router.urls
