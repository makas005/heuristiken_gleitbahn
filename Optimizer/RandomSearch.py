import random

class RandomSearch:
	def __init__(self, dimension, lower_bound, upper_bound, eval_function):
		self.__dimension = dimension			#Anzahl der Stützstellen
		self.__lower_bound = lower_bound		#Untere Grenze des Suchbereichs
		self.__upper_bound = upper_bound		#Obere Grenze des Suchbereichs
		self.__num_tries = 10000				#Anzahl der Versuche
		self.__eval_function = eval_function	#Evaluierungsfunktion

	def Optimize(self):
		#Optimierungsfunktion
		optimal_eval_value = -1							#Bester gefundener Wert
		optimal_vector = [None] * self.__dimension		#Vektor des gefundenen Minimums
		current_vector = [None] * self.__dimension		#Aktueller Vektor

		for t in range(self.__num_tries):
			for d in range(self.__dimension):
				current_vector[d] = random.uniform(self.__lower_bound, self.__upper_bound)

			current_eval_value = self.__eval_function(current_vector)
			if current_eval_value == -1:
				#Fehlerfall
				continue
			if optimal_eval_value == -1:
				#Initialer Schritt
				optimal_eval_value = current_eval_value
				optimal_vector = current_vector.copy()
			elif current_eval_value < optimal_eval_value:
				optimal_eval_value = current_eval_value
				optimal_vector = current_vector.copy()

		return optimal_vector