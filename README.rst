==========================================================
Django Rest Framework MSAL + JWT
==========================================================

.. image:: https://badge.fury.io/py/drf-msal-jwt.svg
    :target: https://badge.fury.io/py/drf-msal-jwt

.. image:: https://travis-ci.org/narongdejsrn/drf-msal-jwt.svg?branch=master
    :target: https://travis-ci.org/narongdejsrn/drf-msal-jwt

.. image:: https://codecov.io/gh/narongdejsrn/drf-msal-jwt/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/narongdejsrn/drf-msal-jwt

This package allows user to authenticate using Microsoft Account in Django REST Framework.

This library rely on `Django REST Framework <https://www.django-rest-framework.org/>`_ and `Django Rest Framework JWT <https://github.com/Styria-Digital/django-rest-framework-jwt>`_ to works properly.
**Please make sure you setup these packages successfully before using this package.**



Documentation
-------------

The full documentation is at https://drf-msal-jwt.readthedocs.io.

Quickstart
----------

Install Django Rest Framework MSAL + JWT::

    pip install drf-msal-jwt

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'drf_msal_jwt',
        ...
    )

Add Django Rest Framework MSAL + JWT's URL patterns:

.. code-block:: python

    from drf_msal_jwt import urls as drf_msal_jwt_urls


    urlpatterns = [
        ...
        url(r'^', include(drf_msal_jwt_urls)),
        ...
    ]

Config the settings.py

.. code-block:: python

    DEFAULTS = {
        'MSAL_CLIENT_ID': "{AZURE_AD_CLIENT_ID}",
        'MSAL_CLIENT_SECRET': "{AZURE_AD_CLIENT_SECRET}",
        'MSAL_AUTHORITY_URL': 'https://login.microsoftonline.com/common/',
        'MSAL_REDIRECT_URL': "{AZURE_AD_REDIRECT_URL}",
        'MSAL_SCOPES': ["User.ReadBasic.All"],
        'MSAL_USER_HANDLER': 'django.contrib.auth.models.User',
        'MSAL_ALLOW_DOMAINS': ['*'],
        'MSAL_CHECK_STATE': True
    }

Features
--------

* [API] for generating Microsoft Login URL
* [API] for logging/creating user based on Authorization Code, and generate JWT token

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox
