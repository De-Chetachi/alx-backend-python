#!/usr/bin/env python3
'''this module contains a  type-annotated function sum_list'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    sums the entries of a given list of floats
    params: input_list a list of floats
    return: sum of list elements
    '''

    return sum(input_list)
