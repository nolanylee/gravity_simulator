import numpy as np
import pygame, sys
import time
import src.physics as physics
from src.objects import Object

#Class representation for simulator. Controls pygame display and interactive parts. 
class Simulation:
	def __init__(self):
		self.run = False
		self.time = False
		self.draw = False
		self.space = None
		self.objs = np.array([])
		self.width = None
		self.height = None
		#default is in solar values (mass and radius of Sun in cgs)
		self.mass, self.velocity, self.force, self.radius, self.position = 1 * 10 ** 11, np.array([0, 0]), np.array([0, 0]), 10, np.array([0, 0])

	#Start simulation, initialize window and run boolean.
	def start_env(self):
		self.run = True
		plane_size = (1080, 600)
		self.width, self.height = plane_size[0], plane_size[1]

		pygame.init()
		pygame.display.set_caption("Gravity Simulator")
		self.space = pygame.display.set_mode(plane_size)

	#Function to display simulation and handle interactive parts
	def show_env(self):
		while self.run:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.run = False

				#ON/OFF button for time (logic)
				if event.type == pygame.MOUSEBUTTONDOWN:
					if self.width/8 <= mousepos[0] <= self.width/8+100 and self.height/2 <= mousepos[1] <= self.height/2+40:
						if self.time:
							self.time = False
						else:
							self.time = True

				#ON/OFF button for draw (logic)
					elif self.width/8 <= mousepos[0] <= self.width/8+100 and self.height/3 <= mousepos[1] <= self.height/3+40:
						if self.draw:
							self.draw = False
						else:
							self.draw = True

				#CLEAR button (logic)
					elif self.width/8 <= mousepos[0] <= self.width/8+100 and self.height/3 * 2 <= mousepos[1] <= self.height/3 * 2+40:
						self.objs = np.array([])

				#place objects at mouse cursor
					else:
						if self.draw:
							new_obj = potential_obj
							self.objs = np.append(self.objs, new_obj)

			mousepos = pygame.mouse.get_pos()

			self.space.fill((0, 0, 0))

			potential_obj = Object(self.mass, self.velocity, self.force, self.radius, mousepos)

			#preview image of object follows mouse
			if self.draw == True:
				pygame.draw.circle(self.space, (255, 255, 255), mousepos, self.radius)

			#ON/OFF button for time (display)
			if self.time == True:
				pygame.draw.rect(self.space, (30, 180, 30),[self.width/8, self.height/2, 100, 40])
				self.space.blit(pygame.font.SysFont('Times New Roman', 35).render('ON', True, (255, 255, 255)), (self.width/8 + 22.5, self.height/2))

				physics.force_update_all(self.objs)
			else:
				pygame.draw.rect(self.space, (180, 30, 30),[self.width/8, self.height/2, 100, 40])
				self.space.blit(pygame.font.SysFont('Times New Roman', 35).render('OFF', True, (255, 255, 255)), (self.width/8 + 17.5, self.height/2))

			#ON/OFF button for draw (display)
			if self.draw == True:
				pygame.draw.rect(self.space, (30, 180, 30),[self.width/8, self.height/3, 100, 40])
				self.space.blit(pygame.font.SysFont('Times New Roman', 30).render('DRAW', True, (255, 255, 255)), (self.width/8 + 5, self.height/3 + 2))

			else:
				pygame.draw.rect(self.space, (180, 30, 30),[self.width/8, self.height/3, 100, 40])
				self.space.blit(pygame.font.SysFont('Times New Roman', 30).render('DRAW', True, (255, 255, 255)), (self.width/8 + 5, self.height/3 + 2))

			#button for clearing objects
			pygame.draw.rect(self.space, (70, 70, 255),[self.width/8, self.height/3 * 2, 100, 40])
			self.space.blit(pygame.font.SysFont('Times New Roman', 25).render('CLEAR', True, (255, 255, 255)), (self.width/8 + 10, self.height/3 * 2 + 5))

			for obj in self.objs:
				obj.draw(self.space)

			if self.time == True:
				for obj in self.objs:
					obj.move()

			time.sleep(0.0005)
			pygame.display.update()



