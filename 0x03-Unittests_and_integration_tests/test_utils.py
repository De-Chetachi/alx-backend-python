#!/usr/bin/env python3
'''unittests for utils.nested_map'''

import unittest
from parameterized import parameterized
from utils import access_nested_map as an_map

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, n_map, key, expected):
        '''to test that the nested map
        produces desired output for given key'''
        self.assertEqual(an_map(n_map, key), expected)


    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
        ])
    def test_access_nested_map_exception(self, n_map, key):
        '''test that an_map raises keyerror for non existent keys'''
        with self.assertRaises(KeyError, msg=key):
            an_map(n_map, key)


if __name__ == '__main__':
    unittest.main()
