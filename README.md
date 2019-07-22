# Names

[![pypi](https://img.shields.io/pypi/v/django-names.svg)](https://pypi.org/project/django-names/)
[![pypi](https://img.shields.io/pypi/pyversions/django-names.svg)](https://pypi.org/project/django-names/)
[![codecov](https://codecov.io/gh/jcp/django-names/branch/master/graph/badge.svg)](https://codecov.io/gh/jcp/django-names)
[![Build Status](https://travis-ci.org/jcp/django-names.svg?branch=master)](https://travis-ci.org/jcp/django-names)

Names is a reusable app for Django that provides mixins, models and form fields
to store a full name and its individual components. The following name
components are supported:

- Full name
- Title
- First name
- Middle name
- Last name
- Suffix
- Nickname

Names officially supports the following:

* Python 3.6 - 3.7
* Django 1.11, 2.0 - 2.2

## Table of Contents

* [Installation](#installation)
* [Basic Usage](#basic-usage)
* [Features](#features)
  * [Name model](#name)
  * [NameField model field](#namefield)
  * [NameModelMixin mixin](#namemodelmixin)
* [Settings](#settings)


## Installation

To install, simply use [pipenv](http://pipenv.org/) (or pip):

```bash
>>> pipenv install django-names
```

Add `names` to your `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = [
    ...
    "names",
]
```

Run migrations:

```bash
>>> python manage.py migrate names
```

## Basic Usage

```bash
>>> from names.models import Name
>>> name = Name.objects.create(full="Natalia Alianovna 'Natasha' Romanova")
>>> name.full
'Natalia Alianovna Romanova (Natasha)'
>>> name.first
'Natalia'
>>> name.middle
'Alianovna'
>>> name.last
'Romanova'
>>> name.nickname
'Natasha'
```

## Features

Names was designed to be flexible. It comes with three primary features:

- [`Name`](#name-model): A model that parses and stores full names.
- [`NameField`](#namefield-model-field): A model field that provides a one-to-one relationship to a `Name` instance.
- [`NameModelMixin`](#namemodelmixin-mixin): A mixin that can be used to extend existing models.

### `Name` model

The `Name` model contains fields and methods that store a full name and its
individual components.

```bash
>>> from names.models import Name
>>> name = Name.objects.create(full="Anthony Edward Stark (Tony)")
>>> name
<Name: Anthony Edward Stark (Tony)>
>>> name.full
'Anthony Edward Stark (Tony)'
>>> name.title
''
>>> name.first
'Anthony'
>>> name.middle
'Edward'
>>> name.last
'Stark'
>>> name.suffix
''
>>> name.nickname
'Tony'
```

When you update an individual name component, the full name updates
automatically when the instance is saved.

```bash
>>> name.nickname = "Iron Man"
>>> name.save()
>>> name.full
'Anthony Edward Stark (Iron Man)'
```

### `NameField` model field

`NameField` has a one-to-one relationship to a `Name` instance.

```python
from names.fields import NameField

class User(models.Model):
    name = NameField(on_delete=models.CASCADE)
```

```bash
>>> from names.models import Name
>>> name = Name.objects.create(full="Carol Susan Jane Danvers")
>>> User = User.objects.create(name=name)
>>> user.name.full
'Carol Susan Jane Danvers'
```

### `NameModelMixin` mixin

`Name` inherits its functionality from the `NameModelMixin` mixin. You can
use this mixin to extend existing models to avoid adding a field with a
one-to-one relationship or additional database tables.

```python
from names.mixins import NameModelMixin

class User(NameModelMixin):
    pass
```

```bash
>>> user = User.objects.create(full="General Nicholas Joseph 'Nick' Fury")
>>> user.full
'General Nicholas Joseph Fury (Nick)'
>>> user.title
'General'
```

## Settings

Names uses the `NAME_SETTINGS` namespace for all settings. The following settings
are supported:

* [MAX_LENGTH](#max_length)
* [STRING_FORMAT](#string_format)
* [EMPTY_ATTRIBUTE_DEFAULT](#empty_attribute_default)
* [OPTIONS](#options)
  * TITLES
  * FIRST_NAME_TITLES
  * SUFFIX_ACRONYMS
  * SUFFIX_NOT_ACRONYMS
  * CONJUNCTIONS
  * PREFIXES
  * CAPITALIZATION_EXCEPTIONS
  * REGEXES

### MAX_LENGTH

`type <int>`

Max length of each `CharField` defined in the `NameModelMixin` mixin.

Default:
```python
100
```

### STRING_FORMAT

`type <str>`

Sets the output string for the `full` field.

**Default**
```python
"{title} {first} {middle} {last} {suffix} ({nickname})"
```

> **Learn more**
>
> [Change the output string with string formatting](https://nameparser.readthedocs.io/en/latest/usage.html#change-the-output-string-with-string-formatting)

### EMPTY_ATTRIBUTE_DEFAULT

`type <str>`

Value returned by empty name attributes.

**Default**
```python
""  # empty string
```

### OPTIONS

`type <dict>`

Handles recognition of titles, prefixes, suffixes and conjunctions. The `OPTIONS` setting is
very powerful and can be used to customize how you parse names.

**Default**
```python
"OPTIONS": {
   "TITLES": TITLES,
   "SUFFIX_NOT_ACRONYMS": SUFFIX_NOT_ACRONYMS,
   "CONJUNCTIONS": CONJUNCTIONS,
   "PREFIXES": PREFIXES,
   "CAPITALIZATION_EXCEPTIONS": CAPITALIZATION_EXCEPTIONS,
   "REGEXES": REGEXES,
}
```

*Options are imported from [`python-nameparser`](https://github.com/derek73/python-nameparser), which is the library used to parse names.*

> **Learn more**
>
> [Editable attributes](https://nameparser.readthedocs.io/en/latest/customize.html#editable-attributes-of-nameparser-config-constants)
