import random

co_ord= []

def create_random_obstacles():
    """Creates our random obstacles
    """
    global co_ord
    co_ord = []

    start_x = -99
    end_x = 97
    start_y = -199
    end_y = 197


    for i in range(10):
        create_horiz_line(start_x,end_x,end_y-1)            #top
        create_horiz_line(start_x,end_x,start_y-1)        #bottom
        create_verti_line(start_y,end_y,start_x-1)        #left
        create_verti_line(start_y,end_y,end_x-1)          #right

        start_x += 10
        end_x -= 10
        start_y += 10
        end_y -= 10


def create_horiz_line(start_x,end_x,y):
    door = random.randrange(start_x+5,end_x-10,5)

    for i in range(start_x,end_x,5):
        if i == door or i == door+4:
            continue
        if i < door:
            point = (i-1,y)
        else:
            point = (i,y)
        co_ord.append(point)


def create_verti_line(start_y,end_y,x):
    door = random.randrange(start_y+5,end_y-10,5)

    for i in range(start_y,end_y,5):
        if i == door or i == door+4:
            continue
        if i < door:
            point = (x,i-1)
        else:
            point = (x,i)
        co_ord.append(point)


def is_position_blocked(x, y):
    for i in co_ord:
        if x in range(i[0],i[0]+5) and y in range(i[1],i[1]+5):
            return True
    return False


def is_path_blocked(x1, x2, y1, y2):
    dir_x = 1 if x1 < x2 else -1
    dir_y = 1 if y1 < y2 else -1

    for x in range(x1,x2+dir_x,dir_x):
        for y in range(y1,y2+dir_y,dir_y):
            if is_position_blocked(x,y):
                return True
    return False


def get_obstacles():
    create_random_obstacles()
    return co_ord