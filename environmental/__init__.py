#!/usr/bin/env python3

"""
Copyright 2015 Zalando SE

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific
language governing permissions and limitations under the License.
"""

import ast
import os
import functools

__not_set = object()


def __env_property(converter: type, key: str, default=__not_set):
    def getter(self):
        value = os.environ.get(key, default)
        if value is __not_set:
            raise AttributeError
        return converter(value)

    def setter(self, value):
        os.environ[key] = str(converter(value))  # use converter to ensure it will store the right type

    new_property = property(getter, setter)
    return new_property


def _make_safe(wanted_type: type):
    def _safe(representation: str):
        if isinstance(representation, wanted_type):
            return representation
        elif isinstance(representation, str):
            return wanted_type(ast.literal_eval(representation))
        else:
            raise ValueError
    return _safe


_safe_bool = _make_safe(bool)
_safe_list = _make_safe(list)
_safe_set = _make_safe(set)
_safe_tuple = _make_safe(tuple)

Bool = functools.partial(__env_property, _safe_bool)
Complex = functools.partial(__env_property, complex)
Float = functools.partial(__env_property, float)
Int = functools.partial(__env_property, int)
List = functools.partial(__env_property, _safe_list)
Str = functools.partial(__env_property, str)
Set = functools.partial(__env_property, _safe_set)
Tuple = functools.partial(__env_property, _safe_tuple)

# TODO: Unit testing
