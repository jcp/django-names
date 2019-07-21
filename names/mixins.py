# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _
from nameparser import HumanName
from nameparser.config import CONSTANTS

from .conf import settings


class NameModelMixin(models.Model):
    """
    An abstract base class model mixin that contains a full name
    and its individual components.
    """

    DEFAULTS = {"max_length": settings.MAX_LENGTH, "blank": True}
    full = models.CharField(verbose_name=_("Full name"), max_length=settings.MAX_LENGTH)
    title = models.CharField(verbose_name=_("Title"), **DEFAULTS)
    first = models.CharField(verbose_name=_("First name"), **DEFAULTS)
    last = models.CharField(verbose_name=_("Last name"), **DEFAULTS)
    middle = models.CharField(verbose_name=_("Middle name"), **DEFAULTS)
    nickname = models.CharField(verbose_name=_("Nickname"), **DEFAULTS)
    suffix = models.CharField(verbose_name=_("Suffix"), **DEFAULTS)

    # Stores previous value of `full`
    _initial = None

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        """
        Stores `self.full` for comparison in `save` method.
        """
        super().__init__(*args, **kwargs)
        self._initial = self.full

    def __str__(self):
        return self.full

    def save(self, *args, **kwargs):
        """
        Parses and saves a full name and its individual components.
        """
        # Use  name components to create a full name. This ensures
        # modifications to individual name components are reflected
        # in the full name.
        name = CONSTANTS.string_format.format(**self.__dict__)

        # If this is a new instance, or `self.full` has been modified,
        # use `self.full` for the full name.
        if not self.pk or self._initial != self.full:
            name = self.full

        instance = self._parse(name=name)
        for attr, val in instance.as_dict().items():
            setattr(self, attr, val)

        self.full = instance.full_name
        super().save(*args, **kwargs)

    @classmethod
    def _parse(cls, name):
        """
        Parses and returns a `HumanName` instance.
        """
        instance = HumanName(
            full_name=name,
            constants=settings.OPTIONS,
            string_format=settings.STRING_FORMAT,
        )

        return instance
