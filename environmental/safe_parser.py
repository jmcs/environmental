#!/usr/bin/env python3

import ast


def make_safe(wanted_type: type):
    def _safe(representation: str):
        if isinstance(representation, wanted_type):
            return representation
        elif isinstance(representation, str):
            return wanted_type(ast.literal_eval(representation))
        else:
            raise ValueError("Can't parse '{}' as a '{}'".format(representation, wanted_type.__name__))

    return _safe
