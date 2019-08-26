# -*- coding: utf-8 -*-
"""
This is the unittest for ogs6py.
"""
from __future__ import division, absolute_import, print_function

import unittest
from ogs6py import __version__


class TestOGS(unittest.TestCase):
    def setUp(self):
        self.version = __version__

    def test_ogs6py(self):
        print(self.version)


if __name__ == "__main__":
    unittest.main()
