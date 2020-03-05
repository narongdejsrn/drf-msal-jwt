# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import MSALLoginView, MSALLoginWithCodeView

app_name = 'drf_msal_jwt'
urlpatterns = [
    url(r'msal/login_url', MSALLoginView.as_view()),
    url(r'msal/login_with_code', MSALLoginWithCodeView.as_view())
    ]
