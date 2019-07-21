# -*- coding: utf-8 -*-

"""
Names uses the `NAMES_SETTINGS` namespace for all settings. For example, your
`settings.py` file may look like this:

NAMES_SETTINGS = {
    "MAX_LENGTH": 175,
    "STRING_FORMAT": "{title} {first} {middle} {last} {suffix} ({nickname})",
    "OPTIONS": {
        "CAPITALIZATION_EXCEPTIONS": (
            ('md', 'M.D.'),
            ('phd', 'Ph.D.'),
        )
    },
}

This module provides a `settings` object that combines all default
`NAMES_SETTINGS` with user-defined `NAMES_SETTINGS`.
"""

from django.conf import settings as dj_settings
from nameparser.config.capitalization import CAPITALIZATION_EXCEPTIONS
from nameparser.config.conjunctions import CONJUNCTIONS
from nameparser.config.prefixes import PREFIXES
from nameparser.config.regexes import REGEXES
from nameparser.config.suffixes import SUFFIX_ACRONYMS, SUFFIX_NOT_ACRONYMS
from nameparser.config.titles import FIRST_NAME_TITLES, TITLES

DEFAULTS = {
    "MAX_LENGTH": 100,
    "STRING_FORMAT": None,
    "EMPTY_ATTRIBUTE_DEFAULT": "",
    "OPTIONS": {
        "TITLES": TITLES,
        "FIRST_NAME_TITLES": FIRST_NAME_TITLES,
        "SUFFIX_ACRONYMS": SUFFIX_ACRONYMS,
        "SUFFIX_NOT_ACRONYMS": SUFFIX_NOT_ACRONYMS,
        "CONJUNCTIONS": CONJUNCTIONS,
        "PREFIXES": PREFIXES,
        "CAPITALIZATION_EXCEPTIONS": CAPITALIZATION_EXCEPTIONS,
        "REGEXES": REGEXES,
    },
}

ERRORS = {
    "invalid": "Invalid setting '{0}'. Refer to {1} for available settings.",
    "removed": "'{0}' has been removed. Refer to '{1}' for available settings.",
}

SETTINGS_DOC = "https://github.com/jcp/django-names/blob/master/README.md#settings"


class Settings:
    """
    Constructs a `Settings` object to handle improperly configured settings,
    combine default and user-defined settings, and expose settings as properties.

    Example:

      >>> from names.settings import settings
      >>> print(settings.OPTIONS)
    """

    def __init__(self):
        self.defaults = DEFAULTS
        self.user_settings = self._get_user_settings()
        self._setup()

    def _get_user_settings(self):
        """
        Retrieves user-defined settings and handles improperly configured settings.
        """
        settings = getattr(dj_settings, "NAMES_SETTINGS", {})

        for setting in settings:
            if setting not in self.defaults:
                raise AttributeError(ERRORS["invalid"].format(setting, SETTINGS_DOC))

        if "OPTIONS" in settings:
            for const in settings["OPTIONS"]:
                if const not in self.defaults["OPTIONS"]:
                    raise AttributeError(ERRORS["invalid"].format(const, SETTINGS_DOC))

        return settings

    def _setup(self):
        """
        Exposes settings as properties and combines defaults and user-defined settings.
        """
        for setting, default in self.defaults.items():
            setattr(self, setting, self.user_settings.get(setting, default))

        # Add default `OPTIONS` that were omitted from user-defined settings.
        for setting, val in self.defaults["OPTIONS"].items():
            if setting not in self.OPTIONS:
                self.OPTIONS.update({setting: val})


settings = Settings()
