from rest_framework import serializers
from .models import Radiostation


class RadiostationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Radiostation
        fields = ('name', 'genre', 'country', 'adress')