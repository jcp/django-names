# -*- coding: utf-8 -*-

#      ___           ___           ___           ___           ___
#     /__/\         /  /\         /__/\         /  /\         /  /\
#     \  \:\       /  /::\       |  |::\       /  /:/_       /  /:/_
#      \  \:\     /  /:/\:\      |  |:|:\     /  /:/ /\     /  /:/ /\
#  _____\__\:\   /  /:/~/::\   __|__|:|\:\   /  /:/ /:/_   /  /:/ /::\
# /__/::::::::\ /__/:/ /:/\:\ /__/::::| \:\ /__/:/ /:/ /\ /__/:/ /:/\:\
# \  \:\~~\~~\/ \  \:\/:/__\/ \  \:\~~\__\/ \  \:\/:/ /:/ \  \:\/:/~/:/
#  \  \:\  ~~~   \  \::/       \  \:\        \  \::/ /:/   \  \::/ /:/
#   \  \:\        \  \:\        \  \:\        \  \:\/:/     \__\/ /:/
#    \  \:\        \  \:\        \  \:\        \  \::/        /__/:/
#     \__\/         \__\/         \__\/         \__\/         \__\/

"""
Names
~~~~~

Names is a reusable app for Django that provides mixins, models
and form fields to store a full name and its individual components.

:copyright: (c) 2019 James C. Palmer.
:license: BSD 3-Clause, see LICENSE.md for more details.
"""

__title__ = "Names"
__description__ = "Names is a reusable app for Django that provides mixins, models and form fields to store a full name and its individual components."  # noqa E501
__url__ = "https://github.com/jcp/django-names"
__package_name__ = "django-names"
__version__ = "1.0.5"
__author__ = "James C. Palmer"
__author_email__ = "me@jcp.io"
__license__ = "BSD 3-Clause"
__copyright__ = "Copyright (c) 2019 James C. Palmer"

VERSION = __version__

default_app_config = "names.apps.NamesConfig"
