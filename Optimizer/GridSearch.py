import numpy
from .ConsoleProgressBar import progress_bar


class GridSearch:
	"""
	Implementierung des Suchalgorithmus "Grid Search"
	
	Wählt alle Punkte innerhalb eines Rasters aus und evaluiert den
	Funktionswert an diesen	Stellen.   
	Der Vektor mit dem geringsten Funktionswert wird zurückgegeben.
	
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

	grid_size : double
		Schrittweite des Rasters, das durchsucht wird.
		
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
		self.__grid_size = 0.1

	def Optimize(self):
		""" Führt den Optimierungsalgorithmus durch.

		Beginnt bei lower_bound für alle Komponenten des Vektors, erhöht 
		danach schrittweise alle Komponenten und evaluert diese. Jede mögliche
		Kombination wird einmal gebildet und bewertet.

		Returns
		-------
		best_vector : list<double>
			Optimierter Vektor gegebener Dimension.

		"""

		best_vector = numpy.zeros(self.__dimension)  # Vektor des gefundenen Minimums
		# Anzahl der Schritte in einer Dimension
		grid_steps = int((self.__upper_bound-self.__lower_bound)/self.__grid_size)
		current_vector = numpy.zeros(self.__dimension) + \
                    self.__lower_bound  # Aktuelle Vektor

		best_vector = current_vector.copy()
		best_eval = self.__eval_function(best_vector.tolist())  # Gefundenes Minimum
		current_vector[0] -= self.__grid_size

		total_steps = (grid_steps+1)**self.__dimension
		for i in range(total_steps):
			if (i % int(total_steps / 100)) == 0:
				# Für jedes Prozent Fortschritt Fortschrittsleiste aktualisieren
				progress_bar("GridSearch", i, total_steps)
			found_highest_index = False
			current_index = 0
			while found_highest_index == False:
				#Wenn aktuelle Komponente die obere Schranke übersteigt, 
				#nächste Komponente inkrementieren
				current_vector[current_index] += self.__grid_size
				if (current_vector[current_index] > self.__upper_bound):
					current_vector[current_index] = self.__lower_bound
					current_index += 1
				else:
					found_highest_index = True

			# Evaluierung
			current_eval = self.__eval_function(current_vector.tolist())
			if (current_eval < best_eval) and (current_eval != -1):
				#Vektor mit bisher geringstem Funktionswert gefunden
				best_vector = current_vector.copy()
				best_eval = current_eval

		return best_vector.tolist()
