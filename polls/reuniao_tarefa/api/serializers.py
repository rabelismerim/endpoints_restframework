from rest_framework import serializers
from polls.reuniao_tarefa.models import reuniao_tarefa

class ReuniaotarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = reuniao_tarefa
        fields = "__all__"