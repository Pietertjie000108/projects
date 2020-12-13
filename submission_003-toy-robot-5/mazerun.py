import robot
import sys
import import_helper

#import mazes
if len(sys.argv) > 2:
    if 'maze' in sys.argv[2]:
        obstacles = import_helper.dynamic_import('maze.' + sys.argv[2])
    else:
        obstacles = import_helper.dynamic_import('maze.obstacles')
else:
    obstacles = import_helper.dynamic_import('maze.obstacles')

#import worlds
if len(sys.argv) > 1 and sys.argv[1].lower() == "turtle" :
    import world.turtle.world as world
else :
    import world.text.world as world

stored_forward = set()
stored_left_turns = set()
stored_right_turn = set()

end_x = 0
end_y = 0


def next_out_of_bounds():
    """
    """
    if world.current_direction_index == 0 and world.position_y == 200:
        return True
    elif world.current_direction_index == 1 and world.position_x == 100:
        return True
    elif world.current_direction_index == 2 and world.position_y == -200:
        return True
    elif world.current_direction_index == 3 and world.position_x == -100:
        return True
    else:
        return False


def next_blocked():
    """
    """
    if world.current_direction_index == 0:
        return obstacles.is_position_blocked(world.position_x, world.position_y + 1)
    elif world.current_direction_index == 1:
        return obstacles.is_position_blocked(world.position_x + 1, world.position_y)
    elif world.current_direction_index == 2:
        return obstacles.is_position_blocked(world.position_x, world.position_y - 1)
    elif world.current_direction_index == 3:
        return obstacles.is_position_blocked(world.position_x - 1, world.position_y)


def right_blocked():
    """
    """
    if world.current_direction_index == 0:
        return obstacles.is_position_blocked(world.position_x + 1, world.position_y)
    elif world.current_direction_index == 1:
        return obstacles.is_position_blocked(world.position_x, world.position_y - 1)
    elif world.current_direction_index == 2:
        return obstacles.is_position_blocked(world.position_x - 1, world.position_y)
    elif world.current_direction_index == 3:
        return obstacles.is_position_blocked(world.position_x, world.position_y + 1)


def left_blocked():
    """
    """
    if world.current_direction_index == 0:
        return obstacles.is_position_blocked(world.position_x - 1, world.position_y)
    elif world.current_direction_index == 1:
        return obstacles.is_position_blocked(world.position_x, world.position_y + 1)
    elif world.current_direction_index == 2:
        return obstacles.is_position_blocked(world.position_x + 1, world.position_y)
    elif world.current_direction_index == 3:
        return obstacles.is_position_blocked(world.position_x, world.position_y - 1)


def end_selector(name, command):
    """
    """
    global end_x,end_y
    if command.lower() == 'top' or command.lower() == '':
        end_y = 200
        mazerun_y(name)
    elif command.lower() == 'bottom':
        end_y = -200
        mazerun_y(name)
    elif command.lower() == 'left':
        end_x = -100
        mazerun_x(name)
    elif command.lower() == 'right':
        end_x = 100
        mazerun_x(name)


def mazerun_x(name):
    """
    """
    print(' > '+name+' starting maze run..')
    while not next_blocked() and not next_out_of_bounds():
        robot.handle_command(name, 'forward 1')
    while world.position_x != end_x:
        if next_blocked() or next_out_of_bounds():
            if (world.position_x,world.position_y) not in stored_left_turns:
                stored_left_turns.add((world.position_x,world.position_y))
                robot.handle_command(name, 'left')
            elif (world.position_x,world.position_y) not in stored_right_turn:
                stored_right_turn.add((world.position_x,world.position_y))
                robot.handle_command(name, 'right')
            else :
                robot.handle_command(name, 'left')
                robot.handle_command(name, 'left')
                stored_left_turns.discard((world.position_x,world.position_y))
                stored_right_turn.discard((world.position_x,world.position_y))
        elif not right_blocked():
            if (world.position_x,world.position_y) not in stored_right_turn:
                stored_right_turn.add((world.position_x,world.position_y))
                robot.handle_command(name, 'right')
            elif (world.position_x,world.position_y) not in stored_forward:
                stored_forward.add((world.position_x,world.position_y))
                while not next_blocked() and not next_out_of_bounds():
                    robot.handle_command(name, 'forward 1')
            elif (world.position_x,world.position_y) not in stored_left_turns and not right_blocked():
                stored_left_turns.add((world.position_x,world.position_y))
                robot.handle_command(name, 'left')
            else :
                robot.handle_command(name, 'right')
                robot.handle_command(name, 'forward 1')
                stored_forward.discard((world.position_x,world.position_y))
                stored_left_turns.discard((world.position_x,world.position_y))
                stored_right_turn.discard((world.position_x,world.position_y))
        else :
            robot.handle_command(name, 'forward 1')


def mazerun_y(name):
    """
    """
    print(' > '+name+' starting maze run..')
    while not next_blocked() and not next_out_of_bounds():
        robot.handle_command(name, 'forward 1')
    while world.position_y != end_y:
        if next_blocked() or next_out_of_bounds():
            if (world.position_x,world.position_y) not in stored_left_turns:
                stored_left_turns.add((world.position_x,world.position_y))
                robot.handle_command(name, 'left')
            elif (world.position_x,world.position_y) not in stored_right_turn:
                stored_right_turn.add((world.position_x,world.position_y))
                robot.handle_command(name, 'right')
            else :
                robot.handle_command(name, 'left')
                robot.handle_command(name, 'left')
                stored_left_turns.discard((world.position_x,world.position_y))
                stored_right_turn.discard((world.position_x,world.position_y))
        elif not right_blocked():
            if (world.position_x,world.position_y) not in stored_right_turn:
                stored_right_turn.add((world.position_x,world.position_y))
                robot.handle_command(name, 'right')
            elif (world.position_x,world.position_y) not in stored_forward:
                stored_forward.add((world.position_x,world.position_y))
                while not next_blocked() and not next_out_of_bounds():
                    robot.handle_command(name, 'forward 1')
            elif (world.position_x,world.position_y) not in stored_left_turns and not right_blocked():
                stored_left_turns.add((world.position_x,world.position_y))
                robot.handle_command(name, 'left')
            else :
                robot.handle_command(name, 'right')
                robot.handle_command(name, 'forward 1')
                stored_forward.discard((world.position_x,world.position_y))
                stored_left_turns.discard((world.position_x,world.position_y))
                stored_right_turn.discard((world.position_x,world.position_y))
        else :
            robot.handle_command(name, 'forward 1')


def mazerunner(name, command):
    """
    """
    global stored_forward,stored_left_turns,stored_right_turn,end_x,end_y
    stored_forward.clear()
    stored_left_turns.clear()
    stored_right_turn.clear()
    end_x = 0
    end_y = 0
    end_selector(name, command)
    if command == "top" or command == "bottom" or command == "left" or command == "right":
        return True, ''+name+': I am at the ' +command+ ' edge.'
    else :
        return True, ''+name+': I am at the top edge.'