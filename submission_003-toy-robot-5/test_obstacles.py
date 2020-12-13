import unittest
from unittest.mock import patch
import sys
from io import StringIO
from test_base import captured_io
import maze.obstacles as obstacles 
import robot

class test_obstacles(unittest.TestCase):


    def test_create_obstacle(self):
        with captured_io(StringIO('HAL\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 1
            robot.robot_start()

        output = out.getvalue().strip()
        
        self.assertEqual("""What do you want to name your robot? HAL: Hello kiddo!
HAL: Loaded obstacles.
There are some obstacles:
- At position 1,1 (to 5,5)""", output[:130])


    def test_position_blocked(self):

        obstacles.random.randint = lambda a, b: 1
        self.assertTrue(obstacles.is_position_blocked(2,2))


    def test_path_blocked_x(self):
        obstacles.random.randint = lambda a, b: 1
        self.assertTrue(obstacles.is_path_blocked(0,2,50,2))

    def test_path_blocked_y(self):
        obstacles.random.randint = lambda a, b: 1
        obslist = obstacles.get_obstacles()
        self.assertTrue(obstacles.is_path_blocked(2,0,2,50))
