import numpy

class IteratedHillblimber:
	def __init__(self, dimension, lower_bound, upper_bound, eval_function):
		self.__dimension = dimension
		self.__lower_bound = lower_bound
		self.__upper_bound = upper_bound
		self.__eval_function = eval_function
		self.__max_tries = 100						#Anzahl der Versuche
		self.__step_size = 0.01

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
		best_vector = numpy.random.uniform(self.__lower_bound, self.__upper_bound, self.__dimension)	#Vektor des gefundenen Minimums
		best_eval = self.__eval_function(best_vector.tolist())	#Wert des gefundenen Minimums
		for current_try in range(self.__max_tries):
			current_vector = numpy.random.uniform(self.__lower_bound, self.__upper_bound, self.__dimension)	#Aktuelle Vektor
			current_eval = self.__eval_function(current_vector.tolist())	#Aktueller Wert
			while True:
				[new_vector,new_eval] = self.__search_surrounding(current_vector.copy() ,current_vector.copy(), current_eval, 0)
				if(new_eval < current_eval):
					current_vector = new_vector
					current_eval = new_eval
				else:
					#Lokales Minimum gefunden
					break
					

			current_eval = self.__eval_function(current_vector.tolist())
			if(current_eval<best_eval)and(current_eval!=-1):
				best_vector = current_vector
				best_eval = current_eval
		
		return best_vector.tolist()