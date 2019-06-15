import copy
import pygame
import numpy as np
from pygame import *
import time
import random
map1 = []
black = (0, 0, 0)
white = (255, 255, 255)

def input_grid():
    global map1, maxx, maxy
    print('------Grid setup------')
    print('default:50*50')
    maxx = input('input maxx:')
    maxy = input('input maxy:')
    if len(maxx) == 0:
        maxx = 50
    else:
        maxx = int(maxx)
    if len(maxy) == 0:
        maxy = 50
    else:
        maxy = int(maxy)
    print('Grid setup:%d * %d' %(maxx, maxy))
    map1 = np.ones((maxx + 1, maxy + 1))*0
    return 

def input_map(x, y):
    global map1
    map1[x-1][y-1] = 1
    return

def check_round_num(x, y):
    global maxx, maxy, map_before
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
    global maxx, maxy, map_before
    map_before = copy.deepcopy(map1)
    for i in range(maxx):
        for j in range(maxy):
            if (check_round_num(i, j) <= 1 or check_round_num(i, j) >= 4): map1[i][j] = 0
            elif check_round_num(i, j) == 3: map1[i][j] = 1

def generate():
    map1[10][10] = map1[10][11] = map1[10][12] = 1

#main game function        
def play():               
        #initialization
        pygame.init()
        scrn = pygame.display.set_mode((maxx * 10, maxy * 10))
        mainsrf = pygame.Surface((maxx * 10, maxy * 10))
        mainsrf.fill(white)
        generate()
        #game cycle
        while 1:
            time_start = time.time()
            #tracking quitting
            for event in pygame.event.get():
                    if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
            #drawing
            for y in range(maxy):
                    for x in range(maxx):
                            if map1[x][y] == 1:
                                    pygame.draw.rect(mainsrf, black, (x*10, y*10, 10, 10))
                            elif map1[x][y] == 0:
                                    pygame.draw.rect(mainsrf, white, (x*10, y*10, 10, 10))
            life_rule()
            scrn.blit(mainsrf, (0, 0))
            time_end = time.time()
            while(time_end - time_start < next_time):
                time_end = time.time()
            pygame.display.update()


def main():
    global map1, map_before, next_time
    input_grid()
    next_time = 0.5
    play()

main()