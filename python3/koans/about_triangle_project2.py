#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

# You need to finish implementing triangle() in the file 'triangle.py'
from .triangle import *

class AboutTriangleProject2(Koan):
    # The first assignment did not talk about how to handle errors.
    # Let's handle that part now.
    def test_illegal_triangles_throw_exceptions(self):
        # All sides should be greater than 0
        self.assertRaises(TriangleError, triangle(0, 0, 0), triangle(3, 4, -5), triangle(1, 1, 3), triangle(2, 5, 2))
