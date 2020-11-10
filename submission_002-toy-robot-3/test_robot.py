import random
import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import robot

class MyTestCase(unittest.TestCase):

    #test history
    def test_history(self):

        with captured_io(StringIO('HAL\nforward 10\nforward 10\noff\n')) as (out, err):
            robot.robot_start()

        self.assertEquals(robot.get_history(None,None,False), ['forward 10','forward 10','off'])

    def test_replay(self):

        with captured_io(StringIO('HAL\nforward 10\nforward 10\nreplay\noff\n')) as (out, err):
            robot.robot_start()
    
        output = out.getvalue().strip()

        self.assertEquals(output, """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,20).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,30).
 > HAL moved forward by 10 steps.
 > HAL now at position (0,40).
 > HAL replayed 2 commands.
 > HAL now at position (0,40).
HAL: What must I do next? HAL: Shutting down..""")

    def test_silent(self):

        with captured_io(StringIO('HAL\nforward 10\nforward 10\nreplay silent\noff\n')) as (out, err):
            robot.robot_start()
    
        output = out.getvalue().strip()

        self.assertEquals(output, """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,20).
HAL: What must I do next?  > HAL replayed 2 commands silently.
 > HAL now at position (0,40).
HAL: What must I do next? HAL: Shutting down..""")

    def test_reverse(self):

        with captured_io(StringIO('HAL\nforward 10\nforward 5\nreplay reversed\noff\n')) as (out, err):
            robot.robot_start()
    
        output = out.getvalue().strip()

        self.assertEquals(output, """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,20).
 > HAL moved forward by 10 steps.
 > HAL now at position (0,30).
 > HAL replayed 2 commands in reverse.
 > HAL now at position (0,30).
HAL: What must I do next? HAL: Shutting down..""")

    def test_reverse_silent(self):

        with captured_io(StringIO('HAL\nforward 10\nforward 5\nreplay reversed silent\noff\n')) as (out, err):
            robot.robot_start()
    
        output = out.getvalue().strip()

        self.assertEquals(output, """What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 10 steps.
 > HAL now at position (0,10).
HAL: What must I do next?  > HAL moved forward by 5 steps.
 > HAL now at position (0,15).
HAL: What must I do next?  > HAL replayed 2 commands in reverse silently.
 > HAL now at position (0,30).
HAL: What must I do next? HAL: Shutting down..""")

    def test_range(self):

        with captured_io(StringIO('HAL\nforward 3\nforward 2\nforward 1\nreplay 1-2\noff\n')) as (out, err):
            robot.robot_start()
    
        output = out.getvalue().strip()

        self.assertEquals(output,"""What do you want to name your robot? HAL: Hello kiddo!
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,3).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL moved forward by 1 steps.
 > HAL now at position (0,6).
HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,9).
 > HAL moved forward by 2 steps.
 > HAL now at position (0,11).
 > HAL replayed 2 commands.
 > HAL now at position (0,11).
HAL: What must I do next? HAL: Shutting down..""")