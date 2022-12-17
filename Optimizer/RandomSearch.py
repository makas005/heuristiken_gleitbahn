import random
from .ConsoleProgressBar import progress_bar


class RandomSearch:
	"""
	Implementierung des Suchalgorithmus "Random Search"
	
	Wählt zufällige Punkte aus und evaluiert den Funktionswert an diesen
	Stellen. Der Vektor mit dem geringsten Funktionswert wird zurückgegeben.
	
	Attribute
	---------
	dimension : unsigned int
		Dimension des Vektors der vom Algorithmus gebildet wird

	lower_bound : int
        Untere Schranke für Werte, die vom Optimierungsalgorithmus ausgegeben werden
            
    upper_bound : int 
        Obere Schranke für Werte, die vom Optimierungsalgorithmus ausgegeben werden

	num_tries : int
		Anzahl der Durchläufe, in denen Vektoren durch Zufall gebildet werden

    eval_function : function
        Evaluiert Funktionswert des Testvektors anhand des aktuellen getesteten Parameters.
        Muss eine Liste von double akzeptieren und double zurückgeben

    Methoden
    --------
    Optimize()
        Führt den Optimierungsalgorithmus aus, optimiert immer auf niedrigste Werte
	"""

	def __init__(self, dimension, lower_bound, upper_bound, eval_function):
		"""
		Parameter
		----------
		dimension : unsigned int
			Dimension des Vektors der vom Algorithmus gebildet wird

		lower_bound : int
    	    Untere Schranke für Werte, die vom Optimierungsalgorithmus ausgegeben werden
	
    	upper_bound : int 
    	    Obere Schranke für Werte, die vom Optimierungsalgorithmus ausgegeben werden

    	eval_function : function
    	    Evaluiert Funktionswert des Testvektors anhand des aktuellen getesteten Parameters.
    	    Muss eine Liste von double akzeptieren und double zurückgeben

		"""

		self.__dimension = dimension  # Anzahl der Stützstellen
		self.__lower_bound = lower_bound  # Untere Grenze des Suchbereichs
		self.__upper_bound = upper_bound  # Obere Grenze des Suchbereichs
		self.__num_tries = 10000  # Anzahl der Versuche
		self.__eval_function = eval_function  # Evaluierungsfunktion

	def Optimize(self):
		""" Führt den Optimierungsalgorithmus durch.

		Setzt einen Vektor aus Zufallszahlen zusammen, evaluiert diesen,
		und gibt den Vektor, der als bestes evaluiert wurde, zurück.

		Returns
		-------
		best_vector : list<double>
			Optimierter Vektor gegebener Dimension.

		"""
		best_eval_value = -1  # Bester gefundener Wert
		best_vector = [None] * self.__dimension  # Vektor des gefundenen Minimums
		current_vector = [None] * self.__dimension  # Aktueller Vektor

		for current_try in range(self.__num_tries):
			if (current_try % int(self.__num_tries / 100)) == 0:
				# Für jedes Prozent Fortschritt Fortschrittsleiste aktualisieren
				progress_bar("GridSearch", current_try, self.__num_tries)
			for d in range(self.__dimension):
				current_vector[d] = random.uniform(self.__lower_bound, self.__upper_bound)

			current_eval_value = self.__eval_function(current_vector)
			if current_eval_value == -1:
				# Fehlerfall
				continue
			if best_eval_value == -1:
				# Initialer Schritt
				best_eval_value = current_eval_value
				best_vector = current_vector.copy()
			elif current_eval_value < best_eval_value:
				#Vektor mit bisher geringstem Funktionswert gefunden
				best_eval_value = current_eval_value
				best_vector = current_vector.copy()

		return best_vector
