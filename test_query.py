# -*- coding: utf-8 -*-

import unittest
import re
from query import *

class QueryTestCase(unittest.TestCase):

    def test_parse_names(self):
        self.assertEqual(None, parse_names(''))
        self.assertEqual(None, parse_names(' '))
        self.assertEqual(None, parse_names('\t'))
        self.assertEqual(None, parse_names('\r'))
        self.assertEqual(None, parse_names('\n'))
        self.assertEqual(None, parse_names('a'))
        self.assertEqual(None, parse_names(' a'))
        self.assertEqual(None, parse_names(' a\t'))
        self.assertEqual(None, parse_names(' a\t '))
        self.assertEqual(('a', 'b'), parse_names(' a b'))
        self.assertEqual(('a', 'b'), parse_names(' a b '))
        self.assertEqual(('a', 'b'), parse_names(' a　b '))
        self.assertEqual(('a', 'b'), parse_names('a-b'))
        self.assertEqual(('a', 'b'), parse_names('a - b'))
        self.assertEqual(('a', 'b'), parse_names('a〜b'))
        self.assertEqual(('a', 'b'), parse_names('a～b'))
        self.assertEqual(('a', 'b'), parse_names('a－b'))
        self.assertEqual(('a', 'b'), parse_names('a　－　b'))
        self.assertEqual(None, parse_names(' a b c'))

    def test_do(self):
        self.assertEqual({'valid': False, 'title': 'type “from” and “to” station names', 'url': ''}, do(''))
        self.assertEqual({'valid': False, 'title': 'type “from” and “to” station names', 'url': ''}, do(' a '))
        self.assertEqual({'valid': True,  'title': 'Query routes from a to b', 'url': 'http://transit.yahoo.co.jp/search/result?from=a&to=b'}, do(' a b '))

if __name__ == '__main__':
    unittest.main()
