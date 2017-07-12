# -*- coding: utf-8 -*-

'test sub.py'

import unittest

import sys
import os
sys.path.append(os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '../src')))

import sub


class TestSub(unittest.TestCase):
    'test class'
    def test_sub(self):
        'test method'
        self.assertEqual(sub.sub(), 'I am Sub!!')


if __name__ == '__main__':
    unittest.main()
