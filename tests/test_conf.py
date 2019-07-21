# -*- coding: utf-8 -*-

import pytest
from django.conf import settings as dj_settings
from django.test import TestCase

from names.conf import DEFAULTS, settings


class TestConfSettings(TestCase):
    def setUp(self):
        self.defaults = DEFAULTS
        self.settings = settings
        self.user_settings = dj_settings.NAMES_SETTINGS

    def test_defaults_match(self):
        assert self.settings.defaults == self.defaults

    def test_get_user_settings(self):
        assert self.settings.user_settings == self.user_settings

    def test_invalid_user_settings(self):
        with pytest.raises(AttributeError):
            self.user_settings.update({"INVALID": True})
            self.settings._get_user_settings()

    def test_invalid_user_settings_option(self):
        with pytest.raises(AttributeError):
            self.user_settings["OPTIONS"] = {"INVALID": True}
            self.settings._get_user_settings()

    def test_setup(self):
        self.user_settings["MAX_LENGTH"] = 200
        self.settings._setup()
        assert self.settings.MAX_LENGTH == 200

    def test_setup_options(self):
        assert len(self.settings.OPTIONS["PREFIXES"]) > 1
        self.user_settings["OPTIONS"] = {"PREFIXES": ["san"]}
        self.settings._setup()
        assert len(self.settings.OPTIONS["PREFIXES"]) == 1
