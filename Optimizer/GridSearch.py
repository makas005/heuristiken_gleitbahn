import numpy
from .ConsoleProgressBar import progress_bar

class IteratedHillblimber:
	def __init__(self, dimension, lower_bound, upper_bound, eval_function):
		self.__dimension = dimension
		self.__lower_bound = lower_bound
		self.__upper_bound = upper_bound
		self.__eval_function = eval_function
		self.__grid_size = 0.1

	def Optimize(self):
		best_vector = numpy.zeros(self.__dimension)	#Vektor des gefundenen Minimums
		grid_steps = int((self.__upper_bound-self.__lower_bound)/self.__grid_size)	#Anzahl der Schritte in einer Dimension
		current_vector = numpy.zeros(self.__dimension)+self.__lower_bound	#Aktuelle Vektor

		best_vector = current_vector.copy()
		best_eval = self.__eval_function(best_vector.tolist())	#Gefundenes Minimum
		current_vector[0] -=self.__grid_size

		total_steps = (grid_steps+1)**self.__dimension
		for i in range(total_steps):
			if (i % int(total_steps / 100)) == 0:
				#For each percent update progress bar 
				progress_bar("GridSearch", i, total_steps)
			found_highest_index = False
			current_index = 0
			while found_highest_index == False:
				#Durchlaufen des Rasters
				current_vector[current_index] +=self.__grid_size
				if(current_vector[current_index]>self.__upper_bound):
					current_vector[current_index] =self.__lower_bound
					current_index += 1
				else:
					found_highest_index=True
			
			#Evaluierung
			current_eval = self.__eval_function(current_vector.tolist())
			if(current_eval<best_eval)and(current_eval!=-1):
				best_vector = current_vector.copy()
				best_eval = current_eval	

		return best_vector.tolist()