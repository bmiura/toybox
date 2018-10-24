# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *
from time import sleep
import random
from copy import deepcopy


SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720
CELL_SIZE = 10
COL_NUMBER = int(SCREEN_WIDTH / CELL_SIZE)
ROW_NUMBER = int(SCREEN_HEIGHT / CELL_SIZE)
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(u"Life Game")

now_field = [[0 for j in range(ROW_NUMBER)] for i in range(COL_NUMBER)]

sysfont = pygame.font.SysFont(None, 22)
gen = 0

my_x = 0
my_y = 0

run = False

ksk = 0


def random_init(now_field):
	for i in range(COL_NUMBER):
		for j in range(ROW_NUMBER):
			now_field[i][j] = 1 if random.random() < 0.2 else 0

def calc_draw(now_field):
	next_field = deepcopy(now_field)
	for i in range(COL_NUMBER):
		for j in range(ROW_NUMBER):
			count = 0
			count += now_field[(i-1)%COL_NUMBER][(j-1)%ROW_NUMBER]
			count += now_field[(i+0)%COL_NUMBER][(j-1)%ROW_NUMBER]
			count += now_field[(i+1)%COL_NUMBER][(j-1)%ROW_NUMBER]
			count += now_field[(i-1)%COL_NUMBER][(j+0)%ROW_NUMBER]
			count += now_field[(i+1)%COL_NUMBER][(j+0)%ROW_NUMBER]
			count += now_field[(i-1)%COL_NUMBER][(j+1)%ROW_NUMBER]
			count += now_field[(i+0)%COL_NUMBER][(j+1)%ROW_NUMBER]
			count += now_field[(i+1)%COL_NUMBER][(j+1)%ROW_NUMBER]
			if now_field[i][j] == 1 and (2 <= count <= 3):
				next_field[i][j] = 1
			elif now_field[i][j] == 0 and count == 3:
				next_field[i][j] = 1
			else:
				next_field[i][j] = 0

			"""
			if my_x == i and my_y == j:
				print count
			"""

			if next_field[i][j] == 1:
				screen.fill((255,255,255),Rect(CELL_SIZE*i,CELL_SIZE*j,CELL_SIZE,CELL_SIZE))
	return next_field

def stop_draw(now_field):
	for i in range(COL_NUMBER):
		for j in range(ROW_NUMBER):
			if now_field[i][j] == 1:
				screen.fill((255,255,255),Rect(CELL_SIZE*i,CELL_SIZE*j,CELL_SIZE,CELL_SIZE))

while True:
	screen.fill((0,0,0))
	if run:
		now_field = deepcopy(calc_draw(now_field))

		gen += 1
	else:
		stop_draw(now_field)

	pygame.draw.rect(screen,(200,200,0),Rect(CELL_SIZE*my_x,CELL_SIZE*my_y,CELL_SIZE,CELL_SIZE),1)
	display1 = sysfont.render("generation:"+str(gen),True,(255,255,255))
	display2 = sysfont.render("s:stop/start  r:reset&randamize   c:clear  k:sppedup/down  n:next",True,(255,255,255))

	screen.blit(display1,(6,20))
	screen.blit(display2,(6,6))

	pygame.display.update()

	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				sys.exit()
			if event.key == K_LEFT:
				my_x = (my_x-1)%COL_NUMBER
			if event.key == K_RIGHT:
				my_x = (my_x+1)%COL_NUMBER
			if event.key == K_UP:
				my_y = (my_y-1)%ROW_NUMBER
			if event.key == K_DOWN:
				my_y = (my_y+1)%ROW_NUMBER
			if event.key == K_SPACE:
				now_field[my_x][my_y] = 0 if now_field[my_x][my_y] else 1
			if event.key == K_s:
				run = not run
			if event.key == K_r:
				random_init(now_field)
				gen = 0
			if event.key == K_c:
				now_field = [[0 for j in range(ROW_NUMBER)] for i in range(COL_NUMBER)]
				gen = 0
			if event.key == K_k:
				ksk = 0 if ksk else 1
			if event.key == K_n:
				now_field = deepcopy(calc_draw(now_field))
				gen += 1
	if ksk == 0:
		sleep(0.1)

	"""
	count = 0
	count += now_field[(my_x-1)%COL_NUMBER][(my_y-1)%ROW_NUMBER]
	count += now_field[(my_x-0)%COL_NUMBER][(my_y-1)%ROW_NUMBER]
	count += now_field[(my_x+1)%COL_NUMBER][(my_y-1)%ROW_NUMBER]
	count += now_field[(my_x-1)%COL_NUMBER][(my_y-0)%ROW_NUMBER]
	count += now_field[(my_x+1)%COL_NUMBER][(my_y-0)%ROW_NUMBER]
	count += now_field[(my_x-1)%COL_NUMBER][(my_y+1)%ROW_NUMBER]
	count += now_field[(my_x-0)%COL_NUMBER][(my_y+1)%ROW_NUMBER]
	count += now_field[(my_x+1)%COL_NUMBER][(my_y+1)%ROW_NUMBER]
	print(count)
	"""
