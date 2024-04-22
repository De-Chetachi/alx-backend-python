#!/usr/bin/env python3
'''this module contains a  type-annotated function sum_mixed_list'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    sums the entries of a given list of floats and integers
    params: mxd_lst a list of floats and integers
    return: sum of list elements
    '''

    return sum(mxd_lst)
