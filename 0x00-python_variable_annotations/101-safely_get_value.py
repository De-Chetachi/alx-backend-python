#!/usr/bin/env python3
'''annotate a given function'''
from typing import Iterable, Mapping, Union, Sequence
from typing import List, Tuple, Any, Optional, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    '''annotating'''
    if key in dct:
        return dct[key]
    else:
        return default
