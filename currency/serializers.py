from rest_framework import serializers

from .models import ExchargeRate

class ConversionSerializer(serializers.Serializer):
    currency_from = serializers.CharField(max_length=6)
    currency_to = serializers.CharField(max_length=6)
    bid = serializers.DecimalField(max_digits=16, decimal_places=5)
    amount = serializers.DecimalField(max_digits=16, decimal_places=5)
    conversion_amount = serializers.DecimalField(max_digits=16, decimal_places=5)
