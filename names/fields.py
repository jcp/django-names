# -*- coding: utf-8 -*-

from django.db import models


class NameField(models.OneToOneField):
    """
    A name field that has a one-to-one relationship to a `names.Name` instance.
    """

    description = "A full name and its individual components."

    def __init__(self, *args, **kwargs):
        kwargs["to"] = "names.Name"
        super().__init__(*args, **kwargs)
