import uuid

import msal
import requests
from django.utils.crypto import get_random_string

from .exceptions import DomainException, WrongTokenException
from .settings import api_settings
from rest_framework_jwt.settings import api_settings as jwt_api_settings


def get_msal_public_app():
    """
    Get MSAL Public Application
    :return:
    """
    msal_client_id = api_settings.MSAL_CLIENT_ID
    msal_authority_url = api_settings.MSAL_AUTHORITY_URL

    assert (msal_client_id is not None)

    return msal.PublicClientApplication(
        msal_client_id,
        authority=msal_authority_url
    )


def get_msal_confidential_app():
    """
    Get MSAL Confidential Application
    :return:
    """
    msal_client_id = api_settings.MSAL_CLIENT_ID
    msal_client_secret = api_settings.MSAL_CLIENT_SECRET
    msal_authority_url = api_settings.MSAL_AUTHORITY_URL

    assert (msal_client_id is not None)
    assert (msal_client_secret is not None)

    return msal.ConfidentialClientApplication(
        msal_client_id,
        client_credential=msal_client_secret,
        authority=msal_authority_url
    )


def build_auth_url(scopes=None, state=None):
    """
    Generate Auth URL

    :param scopes: Permission the client request from the user
    :param state: State string to verify the integrity of the response
    :return:
     - string: a url for user to authenticate
    """
    msal_redirect_url = api_settings.MSAL_REDIRECT_URL
    msal_scopes = api_settings.MSAL_SCOPES

    return get_msal_public_app().get_authorization_request_url(
        scopes or msal_scopes,
        state=state or str(uuid.uuid4()),
        redirect_uri=msal_redirect_url
    )


def get_user_jwt_token(code, scopes=None):
    msal_redirect_url = api_settings.MSAL_REDIRECT_URL
    msal_scopes = api_settings.MSAL_SCOPES
    msal_allow_domains = api_settings.MSAL_ALLOW_DOMAINS

    User = api_settings.MSAL_USER_HANDLER
    tokens = get_msal_confidential_app().acquire_token_by_authorization_code(
        code,
        scopes or msal_scopes,
        redirect_uri=msal_redirect_url
    )

    try:
        microsoft_info = get_microsoft_info(tokens['access_token'])
    except KeyError:
        raise WrongTokenException()

    # check allow domains
    if not '*' in msal_allow_domains:
        if microsoft_info['mail'].split('@')[1] not in msal_allow_domains:
            raise DomainException()

    user = get_user_by_email(microsoft_info['mail'])
    if not user:
        # User not found in the system, we should create a new user
        user = User.objects.create_user(username=tokens['id_token_claims']['preferred_username'],
                                        email=microsoft_info['mail'],
                                        password=get_random_string(length=12),
                                        first_name=microsoft_info.get('givenName', ''),
                                        last_name=microsoft_info.get('surname', ''))
    jwt_payload_handler = jwt_api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = jwt_api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    return token


def get_microsoft_info(access_token):
    r = requests.get(r'https://graph.microsoft.com/v1.0/me/', headers={'Authorization': f'Bearer {access_token}'})
    return r.json()


def get_user_by_email(email):
    User = api_settings.MSAL_USER_HANDLER
    user = User.objects.filter(is_active=True, email=email)
    if not user:
        return None

    return user[0]
