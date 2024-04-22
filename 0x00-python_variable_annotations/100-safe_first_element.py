#!/usr/bin/env python3
'''annotate a given function'''
from typing import Iterable, Union, Sequence, List, Tuple, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''annotatting'''
    if lst:
        return lst[0]
    else:
        return None
