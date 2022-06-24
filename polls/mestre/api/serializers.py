from rest_framework import serializers
from polls.mestre.models import mestre

class MestreSerializer(serializers.ModelSerializer):
    class Meta:
        model = mestre
        fields = "__all__"

