import random

class RandomSearch:
	def __init__(self, dimension, lower_bound, upper_bound, eval_function):
		self.__dimension = dimension
		self.__lower_bound = lower_bound
		self.__upper_bound = upper_bound
		self.__num_tries = 1000
		self.__eval_function = eval_function

	def Optimize(self):
		optimal_eval_value = -1
		optimal_guesses = [None] * self.__dimension
		current_guesses = [None] * self.__dimension

		for t in range(self.__num_tries):
			for d in range(self.__dimension):
				current_guesses[d] = random.uniform(self.__lower_bound, self.__upper_bound)
			current_eval_value = self.__eval_function(current_guesses)
			if current_eval_value == -1:
				#error case
				continue
			if optimal_eval_value == -1:
				optimal_eval_value = current_eval_value
				optimal_guesses = current_guesses.copy()
			elif current_eval_value < optimal_eval_value:
				optimal_eval_value = current_eval_value
				optimal_guesses = current_guesses.copy()


		return optimal_guesses