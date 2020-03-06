from rest_framework.exceptions import APIException


class CodeException(APIException):
    status_code = 500


class DomainException(APIException):
    status_code = 500
