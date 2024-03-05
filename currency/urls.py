from django.urls import path
from .views import ExchargeRateView

app_name = "currency"

urlpatterns = [
    path('currency', ExchargeRateView.as_view()),
]
