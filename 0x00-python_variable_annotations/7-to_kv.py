#!/usr/bin/env python3
'''this module contains a  type-annotated function to_kv'''
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    params: k and an int OR float v as arguments
    returns: tuple.
        The first element of the tuple is the string k.
        The second element is the square of the int/float v
        and should be annotated as a float.
    '''

    return (k, v * v)
