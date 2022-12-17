import numpy
from .ConsoleProgressBar import progress_bar


class IteratedHillblimber:
	"""
	Implementierung des Suchalgorithmus "Iterated Hillclimber"
	
	Wählt zufällig Punkte aus, von denen der Hillclimber-Algorithmus
	angewendet wird. Es wird der minimale Funktionswert gesucht.
	Der minimalste Funktionswert aller ausgewerteter Punkte wird zurückgegeben 
	
	Attribute
	---------
	dimension : unsigned int
		Dimension des Vektors der vom Algorithmus gebildet wird

	lower_bound : int
        Untere Schranke für Werte, die vom Optimierungsalgorithmus ausgegeben werden
            
    upper_bound : int 
        Obere Schranke für Werte, die vom Optimierungsalgorithmus ausgegeben werden

    eval_function : function
        Evaluiert Funktionswert des Testvektors anhand des aktuellen getesteten Parameters.
        Muss eine Liste von double akzeptieren und double zurückgeben

	max_tries : double
		Anzahl der zufälligen Startpunkte, von denen der Algorithmus ausgeführt wird.

	step_size : double
		Schrittweite bei der Interierung des Hillclimber-Algorithmus.

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

		self.__dimension = dimension
		self.__lower_bound = lower_bound
		self.__upper_bound = upper_bound
		self.__eval_function = eval_function
		self.__max_tries = 100  # Anzahl der Versuche
		self.__step_size = 0.01  # Schrittweite bei Hillclimber Iterierung

	def __search_surrounding(self, new_vector, current_vector, current_eval, index):
		""" Sucht in der Umgebung nach besser bewerteten Punkten.

		Manipuliert jedes Element des Vektors (jede Dimension) mithilfe der 
		gegebenen Schrittweite und ermittelt so den besten Funktionswert 
		in der Umgebung. Die Methode wird rekursiv aufgerufen, bis das 
		lokale Minimum gefunden ist.

		Parameter
		---------
		new_vector : list<double>
			Vektor in dem manipulierte Werte getestet werden. Bei initialiem 
			Aufruf gleich dem current_vector.
		
		current_vector : list<double>
			Ursprünglich aufrufender Vektor, der nicht manipuliert wird.
			Muss bis zum Rekursionsende erhalten bleiben. 
			Ist ein günstigerer Vektor gefunden (new_vector), wird der 
			current_vector überschrieben.

		current_eval : double
			Ursprünglich berechneter Funktionswert des Vektors,
			der nicht manipuliert wird. 
			Muss bis zum Rekursionsende erhalten bleiben.

		index : unsigned int
			Index der im aktuellen Rekursionsschritt manipuliert wird.

		Returns
		-------
		current_vector : list<double>
			Vektor zum lokalen Minimum.

		current_eval : double
			Lokales Minimum.

		"""

		if index < self.__dimension:
			# Zwischenspeicherung des aktuellen Vektorelements
			value_at_index = new_vector[index]
			for i in range(-1, 2):
				new_vector[index] = value_at_index
				new_vector[index] = new_vector[index]+self.__step_size*i
				if ((new_vector[index] <= self.__upper_bound) and (new_vector[index] >= self.__lower_bound)):
					[current_vector, current_eval] = self.__search_surrounding(
						new_vector.copy(), current_vector.copy(), current_eval, index+1)
		else:
			# Abbruchbedingung der Rekursion: Alle Dimensionen durchlaufen
			new_eval = self.__eval_function(new_vector.tolist())
			if (new_eval < current_eval) and (current_eval != -1):
				current_eval = new_eval
				current_vector = new_vector.copy()
		return [current_vector, current_eval]

	def Optimize(self):
		""" Führt den Optimierungsalgorithmus durch.

		Wählt zufällig Werte für alle Komponenten des Vektors aus.
		Von diesen Stellen wird der search_sourrounding Algorithmus
		rekursiv aufgerufen, bis ein lokales Minimum gefunden ist.
		Der Vektor mit dem geringsten Funktionswert wird zurückgegeben.

		Returns
		-------
		best_vector : list<double>
			Optimierter Vektor gegebener Dimension.

		"""

		best_vector = numpy.random.uniform(
			self.__lower_bound, self.__upper_bound, self.__dimension)  # Vektor des gefundenen Minimums
		best_eval = self.__eval_function(
			best_vector.tolist())  # Wert des gefundenen Minimums
		for current_try in range(self.__max_tries):
			if (current_try % int(self.__max_tries / 100)) == 0:
				# For each percent update progress bar
				progress_bar("Iterated Hillclimber", current_try, self.__max_tries)
			current_vector = numpy.random.uniform(
				self.__lower_bound, self.__upper_bound, self.__dimension)  # Aktuelle Vektor
			current_eval = self.__eval_function(
				current_vector.tolist())  # Aktueller Wert
			while True:
				[new_vector, new_eval] = self.__search_surrounding(
					current_vector.copy(), current_vector.copy(), current_eval, 0)
				if (new_eval < current_eval):
					current_vector = new_vector
					current_eval = new_eval
				else:
					# Lokales Minimum gefunden, Abbruchbedingung
					break

			current_eval = self.__eval_function(current_vector.tolist())
			if (current_eval < best_eval) and (current_eval != -1):
				#Vektor mit bisher geringstem Funktionswert gefunden
				best_vector = current_vector.copy()
				best_eval = current_eval

		return best_vector.tolist()
