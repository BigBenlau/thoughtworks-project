import copy
import pygame
import numpy as np
from pygame import *
import time
import random
map1 = []
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 200, 1)
red = (200, 2, 0)
grey = (153, 153, 153)
bright_green = (0,255,0)
bright_red = (255,0,0)

def input_grid():
    global map1, maxx, maxy
    print('------Grid setup------')
    print('default:50*50')
    maxx = input('input maxx(<=50, out of = 50):')
    maxy = input('input maxy(<=50, out of = 50):')
    if len(maxx) == 0 or int(maxx) < 0 or int(maxx) > 50:
        maxx = 50
    else:
        maxx = int(maxx)
    if len(maxy) == 0 or int(maxy) < 0 or int(maxy) > 50:
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

def select_map():
    Blinker = [[23,22],[23,23],[23,24]] #Blinker
    Toad = [[23,23],[23,24],[23,25],[24,22],[24,23],[24,24]] #Toad
    Glider = [[22,23],[23,24],[24,22],[24,23],[24,24]] #Glider
    Small_Exploder = [[23,25],[24,24],[24,25],[24,26],[25,24],[26,25],[25,26]] #Small Exploder
    maps = {'Blinker':Blinker,'Toad':Toad,'Glider':Glider,'Small_Exploder':Small_Exploder}
    
    print('------select_map------')
    print(maps.keys())
    print('default:Small_Exploder')
    choice=input('input map name:')
    if len(choice) == 0:
        choice = 'Small_Exploder'
    maplist=maps[choice]
    return maplist

def init_map(map_list):
    for xy in range(len(map_list)):
        x = map_list[xy][0]
        y = map_list[xy][1]
        input_map(x, y)

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

#main game function        
def play():
        global scrn         
        #initialization
        pygame.init()
        map_list=select_map()
        init_map(map_list)
        pygame.display.set_caption('Game of Life')
        scrn = pygame.display.set_mode((1000, 500))
        funsrf = pygame.Surface((500, 500))
        funsrf.fill(grey)
        mainsrf = pygame.Surface((500, 500))
        mainsrf.fill(white)
        game_intro()
        #game cycle
        time_start = time.time()
        check_output = 0
        start = 0
        while 1:
            button("Start",600,30,100,50,green,bright_green,)
            button("Stop",800,30,100,50,red,bright_red,)
            # output
            #tracking quitting
            for event in pygame.event.get():
                    if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
            #drawing
            if check_output == 0:
                for y in range(maxy):
                        for x in range(maxx):
                                if map1[x][y] == 1:
                                        pygame.draw.rect(mainsrf, black, (x*10, y*10, 10, 10))
                                elif map1[x][y] == 0:
                                        pygame.draw.rect(mainsrf, white, (x*10, y*10, 10, 10))
                life_rule()
                scrn.blit(mainsrf, (0, 0))
                scrn.blit(funsrf, (500, 0))
                check_output = 1
            time_end = time.time()
            if(time_end - time_start >= next_time):
                pygame.display.update()
                time_start = time.time()
                check_output = 0
                

def game_intro():
        pygame.draw.rect(scrn, green,(600,30,100,50))
        pygame.draw.rect(scrn, red,(800,30,100,50))

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0] == 1 and x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(scrn, ac,(x,y,w,h))
        if(action != None):
            action()
    else:
        pygame.draw.rect(scrn, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    scrn.blit(textSurf, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def main():
    global map1, map_before, next_time
    input_grid()
    next_time = int(input("State Duration(s): "))
    play()

main()