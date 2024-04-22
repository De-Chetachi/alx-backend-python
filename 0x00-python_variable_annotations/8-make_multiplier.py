#!/usr/bin/env python3
'''this module contains a  type-annotated function make_multiplier'''
from typing import List, Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    params: multiplier
    returns: a function
        that multiplies a float by multiplier.
    '''

    def multiply(n: float, m: float = multiplier) -> float:
        '''multiplying'''
        return n * m
    return multiply
