=============================
Django Rest Framework MSAL + JWT
=============================

.. image:: https://badge.fury.io/py/drf-msal-jwt.svg
    :target: https://badge.fury.io/py/drf-msal-jwt

.. image:: https://travis-ci.org/narongdejsrn/drf-msal-jwt.svg?branch=master
    :target: https://travis-ci.org/narongdejsrn/drf-msal-jwt

.. image:: https://codecov.io/gh/narongdejsrn/drf-msal-jwt/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/narongdejsrn/drf-msal-jwt

Connect Django Rest Framework with MSAL and JWT

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
        'drf_msal_jwt.apps.DrfMsalJwtConfig',
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

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
