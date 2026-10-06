from rest_framework import viewsets
from polls.models import Aluno, Competencia, Mestre, MestreAluno, Reuniao, ReuniaoTarefa
from .serializers import (
    AlunoSerializer, CompetenciaSerializer, MestreSerializer, MestreAlunoSerializer,
    ReuniaoSerializer, ReuniaoTarefaSerializer,
)


class BaseViewSet(viewsets.ModelViewSet):
    ordering = ("-id",)
    ordering_fields = ("id", "dt_criacao")


class MestreViewSet(BaseViewSet):
    queryset = Mestre.objects.all()
    serializer_class = MestreSerializer
    search_fields = ("txt_name", "txt_email", "txt_time")


class AlunoViewSet(BaseViewSet):
    queryset = Aluno.objects.select_related("id_mestre", "id_competencia")
    serializer_class = AlunoSerializer
    search_fields = ("txt_name", "txt_email", "txt_area")


class CompetenciaViewSet(BaseViewSet):
    queryset = Competencia.objects.all()
    serializer_class = CompetenciaSerializer
    search_fields = ("txt_competencia", "txt_tipo", "txt_cargo")


class MestreAlunoViewSet(BaseViewSet):
    queryset = MestreAluno.objects.select_related("id_mestre", "id_aluno")
    serializer_class = MestreAlunoSerializer
    search_fields = ("txt_ano_fiscal", "id_mestre__txt_name", "id_aluno__txt_name")


class ReuniaoViewSet(BaseViewSet):
    queryset = Reuniao.objects.select_related("id_mestre_aluno")
    serializer_class = ReuniaoSerializer
    search_fields = ("txt_comentario",)


class ReuniaoTarefaViewSet(BaseViewSet):
    queryset = ReuniaoTarefa.objects.select_related("id_reuniao", "id_competencia")
    serializer_class = ReuniaoTarefaSerializer
    search_fields = ("txt_atividade", "txt_observacao")
