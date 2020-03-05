#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test-msal
------------

Tests for MSAL Connection
"""

from django.test import TestCase

from drf_msal_jwt.utils import build_auth_url


class TestMSAL(TestCase):

    def setUp(self):
        pass

    def test_login_url(self):
        login_url = build_auth_url()
        self.assertIsNotNone(login_url)

    def tearDown(self):
        pass
