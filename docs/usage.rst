=====
Usage
=====

This library rely on `Django REST Framework <https://www.django-rest-framework.org/>`_ and `Django Rest Framework JWT <https://github.com/jpadilla/django-rest-framework-jwt>`_ to works properly.
**Please make sure you setup these packages successfully before using this package.**


To use Django Rest Framework MSAL + JWT in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'drf_msal_jwt',
        ...
    )

Before using this package, you'll need to `register your application with the Microsoft Identity Platform <https://docs.microsoft.com/azure/active-directory/develop/quickstart-v2-register-an-app>`_

If you already register then config the settings.py in your app accordingly

.. code-block:: python

    DEFAULTS = {
        'MSAL_CLIENT_ID': "{AZURE_AD_CLIENT_ID}",
        'MSAL_CLIENT_SECRET': "{AZURE_AD_CLIENT_SECRET}",
        'MSAL_REDIRECT_URL': "{AZURE_AD_REDIRECT_URL}",
        'MSAL_AUTHORITY_URL': 'https://login.microsoftonline.com/common/',
        'MSAL_SCOPES': ["User.ReadBasic.All"],
        'MSAL_USER_HANDLER': 'django.contrib.auth.models.User',
        'MSAL_ALLOW_DOMAINS': ['*']
    }

- MSAL_CLIENT_ID: Your app Client ID
- MSAL_CLIENT_SECRET: Your app Client Secret
- MSAL_REDIRECT_URL: Redirect URL when the user logged in successfully
- MSAL_AUTHORITY_URL (optional): Your app `authority URL <https://docs.microsoft.com/bs-latn-ba/azure/active-directory/develop/msal-client-application-configuration>`_
- MSAL_SCOPES (optional): scope that you request from the user (User.ReadBasic.All) currently required
- MSAL_ALLOW_DOMAINS (optional): Limit the domain that the user can use to sign in, * to allows all domains

    Be sure configured permission in azure portal according to permission request in MSAL_SCOPES variable.

Add Django Rest Framework MSAL + JWT's URL patterns:

.. code-block:: python

    from drf_msal_jwt import urls as drf_msal_jwt_urls


    urlpatterns = [
        ...
        url(r'^', include(drf_msal_jwt_urls)),
        ...
    ]

Finally, your client can connect to the backend using these url


Get Login URL
+++++++++++++

.. http:get:: /msal/login_url

    Retrieve a login url

    **Example response**:

    .. sourcecode:: json

        {
            "login_url": "https://login.microsoftonline.com/...."
        }

Login using Code
+++++++++++++++++

.. http:post:: /msal/login_with_code

    Login using authorization code from callback page

    The content of ``body``

    .. sourcecode:: json

        {
            "code": "code from callback url params",
            "state": "state from callback url params"
        }

    **Example response**:

    .. sourcecode:: json

        {
            "token": "JWT_token"
        }
