#import modules
import turtle
import sys
import import_helper

#import obstacles
if len(sys.argv) > 2:
    if 'maze' in sys.argv[2]:
        obstacles = import_helper.dynamic_import('maze.' + sys.argv[2])
    else:
        obstacles = import_helper.dynamic_import('maze.obstacles')
else:
    obstacles = import_helper.dynamic_import('maze.obstacles')
# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

#turtle objects
t = turtle.Turtle()

def start():
    reset_world()
    screen = turtle.Screen()
    pen = turtle.Pen()
    pen.penup()
    pen.setpos(min_x, min_y)
    pen.hideturtle()
    pen.pendown()
    pen.color("Red")
    pen.width(10)
    for i in range(2):
        pen.forward(200)
        pen.left(90)
        pen.forward(400)
        pen.left(90)
    obstacles.get_obstacles()
    t.seth(90)
    t.setpos(0,0)
    # screen.exitonclick()


def update_position(steps, robot_name):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y


    if t.heading() == 90:
        new_y = new_y + steps
    elif t.heading() == 0:
        new_x = new_x + steps
    elif t.heading() == 270:
        new_y = new_y - steps
    elif t.heading() == 180:
        new_x = new_x - steps

    if obstacles.is_path_blocked(position_x,position_y,new_x,new_y):
        return "obs"

    if is_position_allowed(new_x, new_y):
        t.setpos(new_x,new_y)
        position_x = t.xcor()
        position_y = t.ycor()
        return True
    
    return False


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    t.right(90)
    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    t.left(90)
    return True, ' > '+robot_name+' turned left.'


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(t.xcor())+','+str(t.ycor())+').')


def draw_maze():
    '''
    draws random obstacles
    '''
    obst = obstacles.get_obstacles()
    for i in obst:
        t.speed(10000)
        t.penup()
        t.goto(i[0],i[1])
        t.pendown()
        t.goto(i[0] + 4,i[1])
        t.goto(i[0] + 4,i[1]+4)
        t.goto(i[0] ,i[1] + 4)
        t.goto(i[0],i[1])
        t.penup()
        t.home()
        t.left(90)


def reset_world():
    t.home()
    t.seth(90)

draw_maze()

