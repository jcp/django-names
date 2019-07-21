# -*- coding: utf-8 -*-

from django.test import TestCase

from names.models import Name

from .data import TEST_DATA


class TestNameModelMixin(TestCase):
    def setUp(self):
        self.data = TEST_DATA

    def test_initial_attribute(self):
        obj = Name.objects.create(full=self.data["names"]["first"]["initial"])
        assert hasattr(obj, "_initial")

    def test_init_method_initial_assignment(self):
        obj = Name.objects.create(full=self.data["names"]["first"]["initial"])
        assert obj._initial == self.data["names"]["first"]["initial"]

    def test_str_method(self):
        obj = Name.objects.create(full=self.data["names"]["first"]["initial"])
        assert str(obj) == self.data["names"]["first"]["initial"]

    def test_save_with_no_pk(self):
        obj = Name.objects.create(full=self.data["names"]["first"]["initial"])
        assert obj.full == self.data["names"]["first"]["initial"]

    def test_save_with_modified_full_field(self):
        obj = Name.objects.create(full=self.data["names"]["first"]["initial"])
        obj.full = self.data["names"]["second"]["initial"]
        obj.save()
        assert obj.full == self.data["names"]["second"]["initial"]

    def test_save_with_modified_name_component_field(self):
        obj = Name.objects.create(full=self.data["names"]["first"]["initial"])
        obj.nickname = self.data["names"]["first"]["nickname"]
        obj.save()
        assert obj.nickname == self.data["names"]["first"]["nickname"]
        assert obj.full == self.data["names"]["first"]["modified"]

    def test_parse_class_method(self):
        obj = Name._parse(name=self.data["names"]["first"]["initial"])
        assert obj.full_name == self.data["names"]["first"]["initial"]
