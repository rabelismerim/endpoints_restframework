from rest_framework import serializers
from polls import aluno
from polls.aluno.models import aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = aluno
        fields = "__all__"