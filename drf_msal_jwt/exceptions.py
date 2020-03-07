from rest_framework.exceptions import APIException


class CodeException(APIException):
    status_code = 401
    default_detail = 'Invalid authorization code'
    default_code = 'code_error'


class DomainException(APIException):
    status_code = 403
    default_detail = "The account from the domain you sign in are not allowed"
    default_code = 'invalid_domain_error'


class StateException(APIException):
    status_code = 401
    default_detail = 'Invalid state, please try again'
    default_code = 'state_error'


class WrongTokenException(APIException):
    status_code = 401
    default_detail = 'The access token is no longer valid, please try logging in again'
    default_code = 'access_token_error'
