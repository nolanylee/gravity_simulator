import numpy as np
from scipy.constants import G
from src.objects import Object

#########################################
# Physics/Math of Gravity Simulator     #
# ---------------------------------     #
# Equations and calculations go here    #
# by: Nolan Lee							#
#########################################

# Returns magnitude of a vector
def magnitude(vector):
	return np.linalg.norm(vector)

# Returns unit vector of vector
def unit_vector(vector):
	return vector / magnitude(vector)

# Returns gravitational force between two bodies using Newton's 2nd law of universal gravitation, F = G(m_1 * m_2)/r**2
# All units in cgs (mass in g, r in cm)
def F(m1, m2, r):
	return G*m1*m2/r**2

# Returns 2d array of distances between objects organized by order (e.g. distance b/w obj3 and obj5 is at index (2, 4))
def dist_all(obj_array):
	dist_array = []
	for obj in obj_array:
		dist_row = []
		for obj2 in obj_array:
			if obj == obj2:
				dist_row.append(np.array([0, 0]))
			else:
				dist_row.append(np.subtract(obj2.position, obj.position))
		dist_array.append(dist_row)
	return dist_array

# Compute force vectors of all objects given array of all objects
def force_update_all(obj_array):
	forces = np.array([])
	dist_array = dist_all(obj_array)
	obj_enum = [np.array([obj, i]) for i, obj in enumerate(obj_array)]
	for obj in obj_enum:
		force_row = np.array([])
		for obj2 in obj_enum:
			r = dist_array[obj[1]][obj2[1]]
			if (r != 0).all():
				force = F(obj[0].mass, obj2[0].mass, r) * unit_vector(r)
			else: 
				force = 0
			force_row = np.append(force_row, force)
		forces = np.append(forces, force_row)
	net_force = np.array([])
	for force_row in forces:
		net_force = np.append(net_force, np.sum(force_row))
	for obj in obj_enum:
		obj[0].update_force(net_force[obj[1]])

