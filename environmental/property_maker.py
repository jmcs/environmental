#!/usr/bin/env python3

import os

NOT_SET = object()


def env_property(converter: type, key: str, default=NOT_SET):
    def getter(self):
        value = os.environ.get(key, default)
        if value is NOT_SET:
            raise AttributeError
        elif value is default:
            return value
        else:
            return converter(value)

    def setter(self, value):
        os.environ[key] = str(converter(value))  # use converter to ensure it will store the right type

    new_property = property(getter, setter)
    return new_property
