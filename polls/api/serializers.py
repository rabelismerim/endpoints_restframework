from rest_framework import serializers
from polls.models import Aluno, Competencia, Mestre, MestreAluno, Reuniao, ReuniaoTarefa


class PessoaSerializer(serializers.ModelSerializer):
    txt_email = serializers.EmailField(max_length=50, required=False, allow_blank=True)


class MestreSerializer(PessoaSerializer):
    class Meta:
        model = Mestre
        fields = ("id", "txt_name", "txt_time", "txt_email", "bl_usuario_ativo", "dt_criacao", "dt_atualizacao")


class AlunoSerializer(PessoaSerializer):
    class Meta:
        model = Aluno
        fields = (
            "id", "id_competencia", "id_mestre", "txt_name", "txt_time", "txt_email",
            "txt_categoria_cargo", "txt_cargo", "txt_area", "txt_linha_servico",
            "txt_nivel_ingles", "txt_business_chemistry", "bl_usuario_ativo", "dt_criacao", "dt_atualizacao",
        )


class CompetenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competencia
        fields = ("id", "txt_cargo", "txt_tipo", "txt_competencia", "dt_criacao", "dt_atualizacao")


class MestreAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MestreAluno
        fields = ("id", "id_mestre", "id_aluno", "txt_ano_fiscal", "dt_criacao")


class ReuniaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reuniao
        fields = ("id", "txt_comentario", "dt_criacao", "dt_atualizacao", "id_mestre_aluno")


class ReuniaoTarefaSerializer(serializers.ModelSerializer):
    nr_prazo = serializers.IntegerField(min_value=0, required=False, allow_null=True)

    class Meta:
        model = ReuniaoTarefa
        fields = (
            "id", "txt_atividade", "txt_status", "dt_conclusao", "nr_prazo", "txt_observacao",
            "dt_criacao", "dt_atualizacao", "id_reuniao", "id_competencia",
        )
        read_only_fields = ("dt_criacao", "dt_atualizacao")
