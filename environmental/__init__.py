#!/usr/bin/env python3

import functools
import pathlib
from .property_maker import env_property
from .safe_types import safe_bool, safe_list, safe_set, safe_tuple

__all__ = ['Bool', 'Complex', 'Float', 'Int', 'List', 'Path', 'Str', 'Set', 'Tuple']

Bool = functools.partial(env_property, safe_bool)
Complex = functools.partial(env_property, complex)
Float = functools.partial(env_property, float)
Int = functools.partial(env_property, int)
List = functools.partial(env_property, safe_list)
Path = functools.partial(env_property, pathlib.Path)
Set = functools.partial(env_property, safe_set)
Str = functools.partial(env_property, str)
Tuple = functools.partial(env_property, safe_tuple)
