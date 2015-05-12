#!/usr/bin/env python3

import ast
import os
import functools

__not_set = object()


def _safe_list(string_representation):
    return list(ast.literal_eval(string_representation))


def _safe_set(string_representation):
    return set(ast.literal_eval(string_representation))


def _safe_tuple(string_representation):
    return tuple(ast.literal_eval(string_representation))


def __env_property(converter: type, key: str, default=__not_set):
    def getter(self):
        value = os.environ.get(key, default)
        if value is __not_set:
            raise AttributeError
        return converter(value)

    def setter(self, value):
        os.environ[key] = str(value)

    new_property = property(getter, setter)
    return new_property


Bool = functools.partial(__env_property, bool)
Complex = functools.partial(__env_property, complex)
Float = functools.partial(__env_property, float)
Int = functools.partial(__env_property, int)
List = functools.partial(__env_property, _safe_list)
Str = functools.partial(__env_property, str)
Set = functools.partial(__env_property, _safe_set)
Tuple = functools.partial(__env_property, _safe_tuple)

# TODO: Unit testing
