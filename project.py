import numpy as np
import copy
import time
map1 = []


# basic map
# map_list = [[3,2],[3,3],[3,4]] #Blinker
# map_list = [[3,3],[3,4],[3,5],[4,2],[4,3],[4,4]] #Toad
# map_list = [[2,3],[3,4],[4,2],[4,3],[4,4]] #Glider
map_list = [[3,5],[4,4],[4,5],[4,6],[5,4],[6,5],[5,6]] #Small Exploder



def input_grid():
    global map1, maxx, maxy
    print('------Grid setup------')
    print('default:10*10')
    maxx = input('input maxx:')
    maxy = input('input maxy:')
    if len(maxx) == 0:
        maxx = 10
    else:
        maxx = int(maxx)
    if len(maxy) == 0:
        maxy = 10
    else:
        maxy = int(maxy)
    print('Grid setup:%d * %d' %(maxx,maxy))
    map1 = np.ones((maxx + 1, maxy + 1))*0
    return 

def input_map(x, y):  
    global map1
    map1[x-1][y-1] = 1
    return

def init_map(map_list):
    for xy in range(len(map_list)):
        x = map_list[xy][0]
        y = map_list[xy][1]
        input_map(x, y)



def check_round_num(x, y):
    count = 0
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(8): 
        nx = x + dx[i]
        ny = y + dy[i]
        if(nx >= 0 and nx < maxx and ny >= 0 and nx < maxy):
            if map_before[nx][ny] == 1: count += 1
    return count

def life_rule():
    global maxx, maxy
    for i in range(maxx):
        for j in range(maxy):
            if (check_round_num(i, j) <= 1 or check_round_num(i, j) >= 4): map1[i][j] = 0
            elif check_round_num(i, j) == 3: map1[i][j] = 1

def main():
    global map1, map_before
    input_grid()
    init_map(map_list)
    print('-----before-----\n', map1)
    
    next_time = 2
    while 1:
        time_start = time.time()
        map_before = copy.deepcopy(map1)
        life_rule()
        print('-----after-----\n', map1)
        time_end = time.time()
        while(time_end - time_start < next_time):
            time_end = time.time()

main()