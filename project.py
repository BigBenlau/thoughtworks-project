import numpy as np
maxx = 10
maxy = 10
map1 = np.ones((maxx, maxy))*0
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
def check_round_num(x, y):
    count = 0
    for i in range(8): 
        nx = x + dx[i]
        ny = y + dy[i]
        if(nx >= 0 and nx < maxx and ny >= 0 and nx < maxy):
            if map_before[nx][ny]: count += 1
    return count

def life_rule(map_before):
    global map1
    for i in range(maxx):
        for j in range(maxy):
            if (check_round_num(i, j) <= 1 or check_round_num(i, j) >= 4): map1[i][j] = 0
            elif check_round_num(i, j) == 3: map1[i][j] = 1
while 1:
    map_before = map1[:]
    print(map_before)
    life_rule(map_before)
