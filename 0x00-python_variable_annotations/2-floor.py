#!/usr/bin/env python3
"""
2. Basic annotations - floor
"""


def floor(n: float) -> int:
    """
    Returns floor of a float.
    """
    return int(n) if n >= 0 else int(n) - 1
