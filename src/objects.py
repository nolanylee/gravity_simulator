import pygame
import numpy as np

#########################################
# Object Class						    #
# ---------------------------------     #
# Class functions for placed objects    #
# by: Nolan Lee							#
#########################################

# Simulator is updated every 0.0005 seconds, used as t in calculations
TIMESTEP = 0.0005

# Class representation of objects to be placed and interact in the gravity simulator
# Mass, velocity, radius, and position are all parameters that can be altered
# Position, velocity, and force are 2d arrays with x and y components
class Object:
	def __init__(self, mass, velocity, force, radius, position):
		self.mass = mass
		self.velocity = velocity
		self.force = force
		self.radius = radius
		self.position = position

	# Pygame function for drawing object on game screen
	def draw(self, surface):
		pygame.draw.circle(surface, [255, 255, 255], self.position, self.radius)

	# Update velocity given some new velocity
	def update_velocity(self, velocity):
		self.velocity = np.add(self.velocity, velocity)

	# Update force given some new force
	def update_force(self, force):
		self.force = np.add(self.force, force)

	# Move object based on current parameters
	# Position is updated based on x = x_i + vt, where x_i is initial position, v is velocity and t is time
	# Velocity is updated based on v = v_i + (F/m)t, where v_i is initial velocity, F is force, m is mass and t is time
	def move(self):
		self.position = np.add(self.position, self.velocity * TIMESTEP)
		self.velocity = np.add(self.velocity, self.force * TIMESTEP / self.mass)