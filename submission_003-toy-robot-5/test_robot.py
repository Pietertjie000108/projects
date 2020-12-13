import unittest
from unittest.mock import patch
import robot
from robot import *
import sys
from io import StringIO
from world.text import world
from maze import obstacles

class test_robot(unittest.TestCase):
 
    @patch("sys.stdin", StringIO("HAL\nforward 10\nright\nforward 10\nreplay\noff"))
    def test_replay(self):
        obstacles.random.randint = lambda a, b: 0
        sys.stdout = StringIO()
        robot.robot_start()
        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (10,10).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (20,10).
 > HAL turned right.
 > HAL now at position (20,10).
 > HAL moved forward by 10 steps.
 > HAL now at position (20,0).
 > HAL replayed 3 commands.
 > HAL now at position (20,0).
HAL: What must I do next? HAL: Shutting down..
''')


    @patch("sys.stdin", StringIO("HAL\nforward 10\nright\nforward 10\nreplay 2\noff"))
    def test_replay_range(self):
        sys.stdout = StringIO()
        robot.robot_start()
        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (10,10).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (10,10).
 > HAL moved forward by 10 steps.
 > HAL now at position (10,0).
 > HAL replayed 2 commands.
 > HAL now at position (10,0).
HAL: What must I do next? HAL: Shutting down..
''')

    @patch("sys.stdin", StringIO("HAL\nforward 10\nright\nforward 10\nreplay 2-1\noff"))
    def test_replay_range_with_multiple_arguments(self):
        sys.stdout = StringIO()
        robot.robot_start()
        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (10,10).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (10,10).
 > HAL replayed 1 commands.
 > HAL now at position (10,10).
HAL: What must I do next? HAL: Shutting down..
''')
    


    @patch("sys.stdin", StringIO("HAL\nforward 5\nleft\nforward 5\nreplay silent\noff"))
    def test_replay_silent(self):
        sys.stdout = StringIO()
        robot.robot_start()
        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (-5,5).
HAL: What must I do next?  > HAL replayed 3 commands silently.
 > HAL now at position (-10,0).
HAL: What must I do next? HAL: Shutting down..
''')

    @patch("sys.stdin", StringIO("HAL\nforward 5\nleft\nforward 5\nreplay silent 2\noff"))
    def test_replay_silent_range(self):
        sys.stdout = StringIO()
        robot.robot_start()
        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (-5,5).
HAL: What must I do next?  > HAL replayed 2 commands silently.
 > HAL now at position (-5,0).
HAL: What must I do next? HAL: Shutting down..
''')

    @patch("sys.stdin", StringIO("HAL\nforward 10\nright\nforward 10\nforward 10\nreplay silent 2-1\noff"))
    def test_replay_silent_range_with_multiple_arguments(self):
        sys.stdout = StringIO()
        robot.robot_start()
        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (10,10).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (20,10).
HAL: What must I do next?  > HAL replayed 1 commands silently.
 > HAL now at position (30,10).
HAL: What must I do next? HAL: Shutting down..
''')

    @patch("sys.stdin", StringIO("HAL\nforward 5\nleft\nforward 5\nreplay reversed\noff"))
    def test_replay_reversed(self):
        sys.stdout = StringIO()
        robot.robot_start()
        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (-5,5).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (-10,5).
 > HAL turned left.
 > HAL now at position (-10,5).
 > HAL moved forward by 5 steps.
 > HAL now at position (-10,0).
 > HAL replayed 3 commands in reverse.
 > HAL now at position (-10,0).
HAL: What must I do next? HAL: Shutting down..
''')

    @patch("sys.stdin", StringIO("HAL\nforward 5\nleft\nforward 5\nreplay reversed 2\noff"))
    def test_replay_reversed_range(self):
        sys.stdout = StringIO()
        robot.robot_start()
        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (-5,5).
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (-5,5).
 > HAL moved forward by 5 steps.
 > HAL now at position (-5,0).
 > HAL replayed 2 commands in reverse.
 > HAL now at position (-5,0).
HAL: What must I do next? HAL: Shutting down..
''')

    @patch("sys.stdin", StringIO("HAL\nforward 10\nright\nforward 10\nforward 10\nreplay reversed 3-1\noff"))
    def test_replay_reversed_with_multiple_arguments(self):
        sys.stdout = StringIO()
        robot.robot_start()
        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (10,10).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (20,10).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (30,10).
 > HAL turned right.
 > HAL now at position (30,10).
 > HAL replayed 2 commands in reverse.
 > HAL now at position (30,10).
HAL: What must I do next? HAL: Shutting down..
''')



    @patch("sys.stdin", StringIO("HAL\nforward 5\nleft\nforward 5\nreplay reversed silent\noff"))
    def test_replay_reversed_silent(self):
        sys.stdout = StringIO()
        robot.robot_start()
        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (-5,5).
HAL: What must I do next?  > HAL replayed 3 commands in reverse silently.
 > HAL now at position (-10,0).
HAL: What must I do next? HAL: Shutting down..
''')

    @patch("sys.stdin", StringIO("HAL\nforward 5\nleft\nforward 5\nreplay reversed silent 2\noff"))
    def test_replay_reversed_silent_range(self):
        sys.stdout = StringIO()
        robot.robot_start()
        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL turned left.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (-5,5).
HAL: What must I do next?  > HAL replayed 2 commands in reverse silently.
 > HAL now at position (-5,0).
HAL: What must I do next? HAL: Shutting down..
''')

    @patch("sys.stdin", StringIO("HAL\nforward 10\nright\nforward 10\nforward 10\nreplay reversed silent 3-1\noff"))
    def test_replay_reversed_silent_with_multiple_arguments(self):
        sys.stdout = StringIO()
        robot.robot_start()
        self.assertEqual(sys.stdout.getvalue(), '''What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL turned right.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (10,10).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (20,10).
HAL: What must I do next?  > HAL replayed 2 commands in reverse silently.
 > HAL now at position (30,10).
HAL: What must I do next? HAL: Shutting down..
''')