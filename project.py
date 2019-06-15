maxx = 10, maxy = 10
map1[maxr][maxl]
dx = {-1, -1, -1, 0, 0, 1, 1, 1}, dy = {-1, 0, 1, -1, 1, -1, 0, 1}
def check_round_num(x, y):
    count = 0
    for i in range(8): 
        nx = x + dx[i], ny = y + dy[i]
        if(nx >= 0 && nx < maxx && ny >= 0 && nx < maxy && map1[maxr][maxl]) count = count + 1
    return count
    