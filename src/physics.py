import numpy as np
from scipy.constants import G
from src.objects import Object

#########################################
# Physics/Math of Gravity Simulator     #
# ---------------------------------     #
# Equations and calculations go here    #
# by: Nolan Lee							#
#########################################

# Amplifying factor to amplify gravitational effects
amp = 0.25

# Returns magnitude of a vector
def magnitude(vector):
	return np.linalg.norm(vector)

# Returns unit vector of vector
def unit_vector(vector):
	return vector / magnitude(vector)

# Returns gravitational force between two bodies using Newton's 2nd law of universal gravitation, F = G(m_1 * m_2)/r**2
# All units in cgs (mass in g, r in cm)
def F(m1, m2, r):
	return G*m1*m2/((amp*magnitude(r))**2)

# Returns 2d array of distances between objects organized by order (e.g. distance b/w obj3 and obj5 is at index (2, 4))
def dist_all(obj_array):
	dim = len(obj_array)
	dist_array = np.empty((dim, dim), dtype=object)
	obj_enum = [np.array([obj, i]) for i, obj in enumerate(obj_array)]
	for obj in obj_enum:
		for obj2 in obj_enum:
			if obj[0] == obj2[0]:
				dist_array[obj[1], obj2[1]] = np.array([0.0, 0.0])
			else:
				dist_array[obj2[1], obj[1]] = np.subtract(obj[0].position, obj2[0].position) * np.array([1, -1])
	return dist_array

# Compute force vectors of all objects given array of all objects
def force_update_all(obj_array):
	dim = len(obj_array)
	forces = np.empty((dim, dim), dtype=object)
	dist_array = dist_all(obj_array)
	obj_enum = [np.array([obj, i]) for i, obj in enumerate(obj_array)]
	for obj in obj_enum:
		for obj2 in obj_enum:
			r = dist_array[obj[1], obj2[1]]
			if (r != 0).all():
				force = F(obj[0].mass, obj2[0].mass, r) * unit_vector(r)
			else: 
				force = np.array([0.0, 0.0])
			forces[obj[1], obj2[1]] = force
	net_force = np.empty((dim,), dtype=object)
	for i, force_row in enumerate(forces):
		net_force[i] = np.sum(force_row, axis=0)
	print(net_force)
	for obj in obj_enum:
		obj[0].update_force(net_force[obj[1]])
