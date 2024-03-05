import json

from django.test import TestCase

from rest_framework import status

from .payloads import currency

from utils import tests as utils_tests

class CurrencyViewTestCase(TestCase):
    def validate_currency_full_object(self, content):
        
        correct_payload = currency.currency_return_payload
        
        enable_fields = correct_payload.keys()

        for field in content:
            self.assertTrue(field in enable_fields)

        for field in enable_fields:
            self.assertTrue(field in content)

        rx_payload = utils_tests.rx_json(correct_payload)
        rx_content = utils_tests.rx_json(content)
        
        self.assertEqual(rx_payload, rx_content)

    def test_get(self):
        response = self.client.get('/api/currency?from={}&to={}&amount={}'.format('USD', 'BRL', 10.00), follow=True)
        content = json.loads(response.content.decode("utf-8"))
        print(content)

        self.assertTrue(status.is_success(response.status_code))
        self.validate_currency_full_object(content)