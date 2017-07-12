# -*- coding: utf-8 -*-

'test hello.py'

import unittest

import sys
import os
sys.path.append(os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '../../src/pac')))

import hello


class TestHello(unittest.TestCase):
    'test class'
    def test_hello(self):
        'test method'
        self.assertEqual(hello.hello(), 'Hello, ')


if __name__ == '__main__':
    unittest.main()
