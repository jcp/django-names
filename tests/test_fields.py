# -*- coding: utf-8 -*-

from django.test import TestCase

from names.models import Name

from .data import TEST_DATA
from .models import Person


class TestNameField(TestCase):
    def setUp(self):
        self.data = TEST_DATA

    def test_name_field(self):
        name = Name.objects.create(full=self.data["names"]["first"]["initial"])
        obj = Person.objects.create(name=name)
        assert obj.name == name
