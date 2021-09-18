from rest_framework import serializers
from . models import home

class homeSerializer(serializers.ModelSerializer):
    class Meta:
        model = home
        fields = "__all__"