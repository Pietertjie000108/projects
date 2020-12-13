import random


def create_maze():
    '''
    generates the whole maze
    '''
    obst_list = []
    obs_count = random.randint(0,10)
    
    

    for i in range(obs_count):
        random_obstacle = random.randint(-95,95),random.randint(-195,195)
        obst_list.append(random_obstacle)
    return obst_list



def get_obstacles():
    '''
    returns obstacle coordinates
    '''
    
    obst_list = create_maze()  
    return obst_list


def is_position_blocked(x,y):
    '''
    Returns True if position (x,y) is in an obstacle.
    '''
    for i in get_obstacles():
        if i[0] <= x <= i[0]+4 and i[1] <= y <= i[1] +4:
            return True
    return False


def is_path_blocked(x1, y1, x2, y2):
    '''
    returns True if path (x1, y1) or (x2, y2) crosses an obstacle
    '''
    
    if x1 == x2:
        if y1 > y2:
            for y in range(y1,y2,-1):
                if is_position_blocked(x1,y):
                    return True
        else:
            for y in range(y1,y2):
                if is_position_blocked(x1,y):                    
                    return True
    
    if y1 == y2:
        if x1 > x2:
            for x in range(x1,x2,-1):
                if is_position_blocked(x,y1):                  
                    return True
        else:
            for x in range(x1,x2):
                if is_position_blocked(x,y1):              
                    return True

    return False

