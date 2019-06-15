import numpy as np
import copy
import time
maxx = 10
maxy = 10
c = ""
map1 = np.ones((maxx + 1, maxy + 1))*0
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
def check_round_num(x, y):
    count = 0
    for i in range(8): 
        nx = x + dx[i]
        ny = y + dy[i]
        if(nx >= 0 and nx < maxx and ny >= 0 and nx < maxy):
            if map_before[nx][ny] == 1: count += 1
    return count

def life_rule():
    global map1, map_before
    for i in range(maxx):
        for j in range(maxy):
            if (check_round_num(i, j) <= 1 or check_round_num(i, j) >= 4): map1[i][j] = 0
            elif check_round_num(i, j) == 3: map1[i][j] = 1
map1[1][1] = map1[1][2] = map1[2][1] = map1[2][2] = map1[3][3] = map1[3][4] = map1[4][3] = map1[4][4] = 1
next_time = 1
while 1:
    time_start = time.time()
    map_before = copy.deepcopy(map1)
    life_rule()
    print(map1)
    time_end = time.time()
    while(time_end - time_start < next_time):
        time_end = time.time()