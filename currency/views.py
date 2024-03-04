from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ExchargeRate
from .serializers import ExchargeRateSerializer

class ExchargeRateView(APIView):
    def get(self, request):
        pass