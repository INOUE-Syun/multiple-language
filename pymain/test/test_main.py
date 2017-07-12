# -*- coding: utf-8 -*-

'test sub.py'

import unittest

import sys
import os
sys.path.append(os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '../src')))

import main


class TestMain(unittest.TestCase):
    'test class'
    def test_main(self):
        'test method'
        self.assertEqual(main.main(), 'Hello, I am Sub!!')


if __name__ == '__main__':
    unittest.main()
