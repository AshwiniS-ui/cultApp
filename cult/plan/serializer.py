from rest_framework import serializers
from .models import plan


class planSerializer(serializers.ModelSerializer):
    class Meta:
        model = plan
        fields = "__all__"
