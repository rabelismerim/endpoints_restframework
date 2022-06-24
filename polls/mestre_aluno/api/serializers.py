from rest_framework import serializers
from polls.mestre_aluno.models import mestrealuno

class MestrealunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = mestrealuno
        fields = "__all__"