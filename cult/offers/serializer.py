from rest_framework import serializers
from . models import offers

class offersSerializer(serializers.ModelSerializer):
    class Meta:
        model = offers
        fields = "__all__"