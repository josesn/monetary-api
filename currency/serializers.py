from rest_framework import serializers

from .models import ExchargeRate

class ExchargeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchargeRate
        fields = '__all__'