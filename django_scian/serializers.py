from rest_framework import serializers
from .models import SCIAN

class SCIANSerializer(serializers.ModelSerializer):

    class Meta:
        model = SCIAN
        fields = '__all__'