from rest_framework import serializers
from polls.reuniao.models import reuniao

class ReuniaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = reuniao
        fields = "__all__"
