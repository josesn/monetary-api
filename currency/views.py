from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ConversionSerializer
from .conversions import CurrencyApi, CurrencyConversion

class ExchargeRateView(APIView):
    def get(self, request):
        currency_from = request.GET.get('from', "")
        currency_to = request.GET.get('to', "")
        amount = request.GET.get('amount', "")
        
        if currency_from and currency_to and amount:
            currency_api = CurrencyApi()
            currency = CurrencyConversion()
            try:
                call_conversion = currency_api.call_currency_rate(currency_from, currency_to)
                conversion_value = currency.conversion_value(call_conversion.bid, amount)
            
                obj = {
                    "currency_from": currency_from,
                    "currency_to": currency_to,
                    "bid": call_conversion.bid,
                    "amount": amount,
                    "conversion_amount": conversion_value,
                }
                serializer = ConversionSerializer(obj)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        return Response(status=status.HTTP_404_NOT_FOUND)