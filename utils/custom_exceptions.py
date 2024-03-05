from rest_framework.exceptions import APIException

class ApiConversionException(APIException):
    status_code = 404
    default_detail = 'Something wrong. Conversion failed or API may be down at the moment'