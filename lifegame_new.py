# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *
from time import sleep
import random

class LifeGame:
	def __init__(self, screen_width=960, screen_height=720, cell_size=10):
		pygame.init()
		self.screen_size = (screen_width, screen_height)
		self.cell_size = cell_size
		self.screen = pygame.display.set_mode(self.screen_size)
		self.col_number = int(screen_width / cell_size)
		self.row_number = int(screen_height / cell_size)
		pygame.display.set_caption(u"Life Game")
		self.now_field = self.clear_field()
		self.sysfont = pygame.font.SysFont(None, 22)
		self.gen = 0
		self.my_x = 0
		self.my_y = 0
		self.isrun = False
		self.ksk = False

	def clear_field(self):
		return [[0 for j in range(self.row_number)] for i in range(self.col_number)]

	def random_field(self, rate=0.2):
		return [[1 if random.random() < rate else 0 for j in range(self.row_number)] for i in range(self.col_number)]

	def calc(self):
		next_field = self.clear_field()
		for i in range(self.col_number):
			for j in range(self.row_number):
				count = 0
				count += self.now_field[(i-1)%self.col_number][(j-1)%self.row_number]
				count += self.now_field[(i+0)%self.col_number][(j-1)%self.row_number]
				count += self.now_field[(i+1)%self.col_number][(j-1)%self.row_number]
				count += self.now_field[(i-1)%self.col_number][(j+0)%self.row_number]
				count += self.now_field[(i+1)%self.col_number][(j+0)%self.row_number]
				count += self.now_field[(i-1)%self.col_number][(j+1)%self.row_number]
				count += self.now_field[(i+0)%self.col_number][(j+1)%self.row_number]
				count += self.now_field[(i+1)%self.col_number][(j+1)%self.row_number]
				if self.now_field[i][j] == 1 and (2 <= count <= 3):
					next_field[i][j] = 1
				elif self.now_field[i][j] == 0 and count == 3:
					next_field[i][j] = 1
				else:
					next_field[i][j] = 0
		return next_field

	def draw(self):
		self.screen.fill((0,0,0))
		for i in range(self.col_number):
			for j in range(self.row_number):
				if self.now_field[i][j] == 1:
					self.screen.fill((255,255,255),Rect(self.cell_size*i, self.cell_size*j, self.cell_size, self.cell_size))
		pygame.draw.rect(self.screen,(200,200,0), Rect(self.cell_size*self.my_x, self.cell_size*self.my_y, self.cell_size, self.cell_size), 1)
		display1 = self.sysfont.render("generation:"+str(self.gen), True, (255,255,255))
		display2 = self.sysfont.render("s:stop/start  r:reset&randamize   c:clear  k:sppedup/down  n:next", True, (255,255,255))
		self.screen.blit(display1,(6,20))
		self.screen.blit(display2,(6,6))
		pygame.display.update()


	def step(self):
		self.now_field = self.calc()
		self.draw()
		self.gen += 1

	def run(self):
		while True:
			if self.isrun:
				self.step()
			else:
				self.draw()

			for event in pygame.event.get():
				if event.type == QUIT:
					sys.exit()
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						sys.exit()
					if event.key == K_LEFT:
						self.my_x = (self.my_x-1)%self.col_number
					if event.key == K_RIGHT:
						self.my_x = (self.my_x+1)%self.col_number
					if event.key == K_UP:
						self.my_y = (self.my_y-1)%self.row_number
					if event.key == K_DOWN:
						self.my_y = (self.my_y+1)%self.row_number
					if event.key == K_SPACE:
						self.now_field[self.my_x][self.my_y] = 0 if self.now_field[self.my_x][self.my_y] else 1
					if event.key == K_s:
						self.isrun = not self.isrun
					if event.key == K_r:
						self.now_field = self.random_field()
						self.gen = 0
					if event.key == K_c:
						self.now_field = self.clear_field()
						self.gen = 0
					if event.key == K_k:
						self.ksk = False if self.ksk else True
					if event.key == K_n:
						self.step()
			if not self.ksk:
				sleep(0.1)

if __name__ == '__main__':
	lifegame = LifeGame()
	lifegame.run()
