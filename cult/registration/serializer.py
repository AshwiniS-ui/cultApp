from rest_framework import serializers
from . models import registration

class registrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = registration
        fields = ("user_name", "ph_no", "gmail", "password")