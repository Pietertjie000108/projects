import unittest
from unittest.mock import patch
import sys
from io import StringIO
from world.text import world

class test_world(unittest.TestCase):
    def test_is_position_allowed(self):
        position_allowed = world.is_position_allowed(0,10)
        self.assertTrue(position_allowed)

    def test_not_position_allowed(self):
        position_not_allowed = world.is_position_allowed(300,250)
        self.assertFalse(position_not_allowed)

if __name__ == "__main__":
    unittest.main()