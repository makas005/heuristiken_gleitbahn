import numpy

class IteratedHillblimber:
	def __init__(self, dimension, lower_bound, upper_bound, eval_function):
		self.__dimension = dimension
		self.__lower_bound = lower_bound
		self.__upper_bound = upper_bound
		self.__eval_function = eval_function
		self.__delta = 0.1
		self.__delta_min = 0.0001
		self.__alpha = 0.5
	
	def __explore(self, current_vector):
		old_vector = current_vector.copy()
		current_minimum = self.__eval_function(current_vector.tolist())
		for i in range(self.__dimension):
			current_vector[i] += self.__delta
			if(self.__eval_function(current_vector.tolist()) < current_minimum):
				current_minimum = self.__eval_function(current_vector.tolist())
			else:
				current_vector[i] -= 2*self.__delta
				if(self.__eval_function(current_vector.tolist())<current_minimum):
					current_minimum = self.__eval_function(current_vector.tolist())
				else:
					current_vector[i] = old_vector[i]
		return current_vector

	def Optimize(self):
		psi = numpy.random.uniform(self.__lower_bound, self.__upper_bound, self.__dimension)
		while True:
			phi = psi.copy()
			phi = self.__explore(phi.copy())
			if(self.__eval_function(phi.tolist())<self.__eval_function(psi.tolist())):
				while True:
					teta = psi.copy()
					psi = phi.copy()
					phi = phi + self.__alpha * (phi-teta)
					phi = self.__explore(phi.copy())
					if(self.__eval_function(phi.tolist())>=self.__eval_function(psi.tolist())):
						break
			else:
				self.__delta = self.__delta/2
			if(self.__delta<self.__delta_min):
				break
		return psi.tolist()