#!/usr/bin/env python3
'''unittests for utils.nested_map'''

import unittest
from parameterized import parameterized
from utils import access_nested_map as an_map
from utils import get_json, memoize
import requests
from unittest.mock import patch, Mock


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


class TestGetJson(unittest.TestCase):
    '''test class for the get_json funstion in utils'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        '''tests that the get_json method returns the expected result'''

        mock_get.return_value.json.return_value = test_payload

        res = get_json(test_url)
        self.assertEqual(res, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    '''test memoize class'''
    def test_memoize(self):
        '''test memoize'''
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as a_meth:
            test_obj = TestClass()
            self.assertEqual(test_obj.a_property, 42)
            self.assertEqual(test_obj.a_property, 42)
        a_meth.assert_called_once()


if __name__ == '__main__':
    unittest.main()
