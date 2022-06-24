from rest_framework import serializers
from polls.competencia.models import competencia

class CompetenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = competencia
        fields = "__all__"
