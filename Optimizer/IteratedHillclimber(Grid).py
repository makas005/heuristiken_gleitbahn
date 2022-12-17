import numpy
from .ConsoleProgressBar import progress_bar

class IteratedHillblimber:
	def __init__(self, dimension, lower_bound, upper_bound, eval_function):
		self.__dimension = dimension
		self.__lower_bound = lower_bound
		self.__upper_bound = upper_bound
		self.__eval_function = eval_function
		self.__step_size = 0.01
		self.__grid_size = 1 

	def __search_surrounding(self,new_vector,current_vector, current_eval, index):
		if index<self.__dimension:
			value_at_index=new_vector[index]	#Zwischenspeicherung des aktuellen Vektorelements
			for i in range (-1,2):
				new_vector[index] = value_at_index
				new_vector[index] = new_vector[index]+self.__step_size*i
				if((new_vector[index]<=self.__upper_bound)and(new_vector[index]>=self.__lower_bound)):
					[current_vector,current_eval] = self.__search_surrounding(new_vector.copy(),current_vector.copy(), current_eval, index+1)
		else:
			new_eval = self.__eval_function(new_vector.tolist())
			if(new_eval<current_eval)and(current_eval!=-1):
				current_eval = new_eval
				current_vector = new_vector.copy()
		return [current_vector,current_eval]


	def Optimize(self):
		best_vector = numpy.zeros(self.__dimension)
		best_eval = self.__eval_function(best_vector.tolist())
		grid_steps = int((self.__upper_bound-self.__lower_bound)/self.__grid_size)
		
		current_vector = numpy.zeros(self.__dimension)+self.__lower_bound
		current_grid_vector = numpy.zeros(self.__dimension)+self.__lower_bound
		current_grid_vector[0] -=self.__grid_size
		total_steps = (grid_steps+1)**self.__dimension
		for current_try in range(total_steps):
			if (current_try % int(total_steps / 100)) == 0:
				# For each percent update progress bar
				progress_bar("Iterated Hillclimber (Grid)", current_try, total_steps)
			found_highest_index = False
			current_index = 0
			while found_highest_index == False:
				current_grid_vector[current_index] +=self.__grid_size
				if(current_grid_vector[current_index]>self.__upper_bound):
					current_grid_vector[current_index] =self.__lower_bound
					current_index += 1
				else:
					found_highest_index=True
			
			current_vector = current_grid_vector.copy()
			current_eval = self.__eval_function(current_vector.tolist())
			while True:
				[new_vector,new_eval] = self.__search_surrounding(current_vector.copy(), current_vector.copy(), current_eval,0)
				if(new_eval < current_eval):
					current_vector = new_vector.copy()
					current_eval = new_eval
				else:
					#Lokale Minimum
					break
			if(current_eval<best_eval)and(current_eval!=-1):
				best_vector = current_vector.copy()
				best_eval = current_eval
		
		return best_vector.tolist()