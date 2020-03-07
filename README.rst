==========================================================
Django Rest Framework MSAL + JWT
==========================================================

.. image:: https://badge.fury.io/py/drf-msal-jwt.svg
    :target: https://badge.fury.io/py/drf-msal-jwt

.. image:: https://travis-ci.org/narongdejsrn/drf-msal-jwt.svg?branch=master
    :target: https://travis-ci.org/narongdejsrn/drf-msal-jwt

.. image:: https://codecov.io/gh/narongdejsrn/drf-msal-jwt/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/narongdejsrn/drf-msal-jwt

This library allows user to authenticate using Microsoft Account in Django Rest Framework

Documentation
-------------

The full documentation is at https://drf-msal-jwt.readthedocs.io.

Quickstart
----------

This library rely on `Django REST Framework <https://www.django-rest-framework.org/>`_ and `Django Rest Framework JWT <https://github.com/jpadilla/django-rest-framework-jwt>`_ to works properly.
**Please make sure you setup these packages successfully before using this package.**

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

Features
--------

* Generate login url for authentication using Microsoft Account
* Create new user based on Authorization code and generate JWT token for the user to log in

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox
