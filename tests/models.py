# -*- coding: utf-8 -*-

from django.db import models

from names.fields import NameField


class Person(models.Model):
    name = NameField(on_delete=models.CASCADE)

    class Meta:
        app_label = "tests"
