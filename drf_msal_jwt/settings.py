from django.conf import settings
from rest_framework.settings import APISettings

USER_SETTINGS = getattr(settings, 'DRF_MSAL', None)

DEFAULTS = {
    'MSAL_CLIENT_ID': None,
    'MSAL_CLIENT_SECRET': None,
    'MSAL_AUTHORITY_URL': 'https://login.microsoftonline.com/common/',
    'MSAL_REDIRECT_URL': None,
    'MSAL_SCOPES': ["User.ReadBasic.All"],
    'MSAL_USER_HANDLER': 'django.contrib.auth.models.User',
    'MSAL_ALLOW_DOMAINS': ['*'],
    'MSAL_CHECK_STATE': True
}

IMPORT_STRINGS = (
    'MSAL_USER_HANDLER'
)

api_settings = APISettings(USER_SETTINGS, DEFAULTS, IMPORT_STRINGS)
