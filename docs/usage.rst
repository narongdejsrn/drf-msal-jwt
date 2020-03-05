=====
Usage
=====

To use Django Rest Framework MSAL + JWT in a project, add it to your `INSTALLED_APPS`:

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
