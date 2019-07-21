# -*- coding: utf-8 -*-

from django.test import TestCase

from names.admin import NameAdmin


class TestNameAdmin(TestCase):
    def test_name_admin(self):
        assert NameAdmin
