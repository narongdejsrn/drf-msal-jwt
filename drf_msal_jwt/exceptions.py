from rest_framework.exceptions import APIException


class CodeException(APIException):
    status_code = 500
