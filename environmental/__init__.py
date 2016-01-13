#!/usr/bin/env python3

import functools
import pathlib
from typing import Callable
from .property_maker import env_property
from .safe_types import safe_bool, safe_list, safe_set, safe_tuple

__all__ = ['Bool', 'Complex', 'Float', 'Int', 'List', 'Path', 'Str', 'Set', 'Tuple']

Bool = functools.partial(env_property, safe_bool)  # type: Callable[[str, bool], bool]
Complex = functools.partial(env_property, complex)  # type: Callable[[str, complex], complex]
Float = functools.partial(env_property, float)  # type: Callable[[str, float], float]
Int = functools.partial(env_property, int)  # type: Callable[[str, int], int]
List = functools.partial(env_property, safe_list)  # type: Callable[[str, list], list]
Path = functools.partial(env_property, pathlib.Path)  # type: Callable[[str, pathlib.Path], pathlib.Path]
Set = functools.partial(env_property, safe_set)  # type: Callable[[str, set], set]
Str = functools.partial(env_property, str)  # type: Callable[[str, str], str]
Tuple = functools.partial(env_property, safe_tuple)  # type: Callable[[str, tuple], tuple]
