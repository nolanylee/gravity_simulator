import numpy as np
import pygame
from src.objects import Object
from src.physics import *
from src.simulator import Simulation

if __name__ == "__main__":
	print(pygame.QUIT)
	# Object(mass, velocity, force, radius, position)
	sim = Simulation()

	sim.start_env()
	sim.show_env()