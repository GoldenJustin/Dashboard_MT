from rest_framework import serializers
from .models import *


class ReporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporter
        fields = '__all__'


class ScammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scammer
        fields = '__all__'


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'

