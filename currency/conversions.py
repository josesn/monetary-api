import requests
import json
from decimal import Decimal

from .models import ExchargeRate

from utils.custom_exceptions import ApiConversionException

class CurrencyApi:
    """
        Chamada para API Externa para buscar cotação de momento
        Caso API não tenha retorno, buscar no banco de dados o 
        registro mais recente da cotação registrado
    """
    def call_currency_rate(self, currency_from, currency_to):
        try:
            excharge_rate = None
            resp = requests.get("https://economia.awesomeapi.com.br/last/{}-{}".format(currency_from, currency_to))
            if resp.status_code == 200 or 201:
                data = resp.json()
                conversion = "{}{}".format(currency_from, currency_to)
                excharge_rate = ExchargeRate.objects.create(
                    currency_code=data[conversion]['code'],
                    currency_code_in=data[conversion]['codein'],
                    bid=data[conversion]['bid'],
                    ask=data[conversion]['ask'],
                    date_in=data[conversion]['timestamp']
                )
            else:
                excharge_rate = ExchargeRate.objects.filter(
                    currency_code=currency_from,
                    currency_code_in=currency_to,
                ).order_by('-date_in').first()
           
            return excharge_rate
        except:
            raise ApiConversionException

class CurrencyConversion:
    def conversion_value(self, excharge_rate, amount):
        total_value = None
        try:
            total_value = round(Decimal(amount) * Decimal(excharge_rate), 3)
        except:
            raise ValueError('Conversion value failed')
        
        return total_value