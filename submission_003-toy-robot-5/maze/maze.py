import sys, os, random
USER_PATHS = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../'))
sys.path.insert(0, USER_PATHS)

# creating the obstacles lists
obstacles = []

def create_obstacles():
    """
    """
    draw_lines(20, -10, 20, 50)
    draw_lines(20, 50, -20, 50)
    draw_lines(-20, 50, -20, -10)

    draw_lines(40, -10, 20, -10)
    draw_lines(40, -10, 40, -50)
    draw_lines(40 , -50,  -40, -50)
    draw_lines(-40, 100, -40, -50)
    
    draw_lines(60, 80, 0, 80)

    draw_lines(60, 100, -60, 100)
    draw_lines(60, -100, -60, -100)
    draw_lines(60, 100, 60, -100)
    draw_lines(-60, 100, -60, -60)

    draw_lines(-80, 150, -80, -150)
    draw_lines(-80, -150, 92, -150)
    draw_lines(80, 150, -80, 150)

    draw_lines(80, 146, 80, -134)
    draw_lines(96, 192, 96, -150)
    draw_lines(92, 196, -20, 196)
    draw_lines(-50, 196, -100, 196)
    return obstacles


def is_position_blocked(x,y):
    """
    foreach set of tuples inside of the obstacles lists, it checks if the position of either x or y (which is the robot passed position) is in the range of the obstacle, 
    :returns True if the position is blocked:
    :returns False if the position is not blocked:
    """
    for tups in obstacles:
        tup_x = tups[0]
        tup_y = tups[1]
        if (tup_x <= x <= (tup_x + 4)) and (tup_y <= y <= (tup_y + 4)):
            return True
    return False


def is_path_blocked(x1, y1, x2, y2):
    """
    takes the min and max values passed through with x1 and y1 being the co-ords
    that you are at and x2 and y2 the co-ords that you are moving to. and checks
    that if the position you are moving towards has an obstacle in the way
    :returns True if the path is blocked:
    :returns False if the path is not blocked:
    """

    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)

    if x1 == x2:
        for i in range(min_y, max_y + 1):
            if is_position_blocked(x1, i) :
                return True
    elif y1 == y2:
        for i in range(min_x, max_x + 1):
            if is_position_blocked(i, y1):
                return True
    return False


def draw_lines(old_x, old_y, new_x, new_y):
    global obstacles

    min_x = min(old_x, new_x)
    max_x = max(old_x, new_x)
    min_y = min(old_y, new_y)
    max_y = max(old_y, new_y)

    if old_y == new_y:
        for i in range(min_x, max_x + 5, 5):
            obstacles.append((i, old_y))
    elif old_x == new_x:
        for i in range(min_y, max_y + 5, 5):
            obstacles.append((old_x, i))
    return obstacles


def get_obstacles():
    create_obstacles()
    return obstacles