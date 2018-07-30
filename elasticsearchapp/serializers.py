from rest_framework import serializers
from .models import Disease

class DiseaseSerializer(serializers.Serializer):
    def create(self, validated_data):
        return Disease.objects.create(**validated_data)

    class Meta:
        model = Disease
