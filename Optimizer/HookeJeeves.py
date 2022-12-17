import numpy


class HookeJeeves:
	"""
	Implementierung des Suchalgorithmus nach Hooke und Jeeves
	
	Wählt einen zufälligen Punkt im Suchbereich aus, tastet sich
	von dort aus in alle Richtungen vor und versucht die Evaluierungs-
	funktion zu minimieren. Anschließend wird laufend im Suchfeld vorran-
	geschritten, evaluiert und anschließend die Schrittgröße halbiert, 
	bis die	Schrittweite unter einem zuvor definierten Minimum liegt. 
	
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

	delta : double
		Initiale Schrittweite zur Annäherung an den optimalen Vektor.
		
	delta_min : double
		Minimale Schrittweite zur Annäherung an den optimalen Vektor.
		Ist diese erreicht, wird die weitere Annähreung abgebrochen.

	alpha : double
		Faktor des Vorranschreitens im Suchgebiet.

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
		self.__delta = 0.1
		self.__delta_min = 0.0001
		self.__alpha = 0.5

	def __explore(self, current_vector):
		""" Tastet im Umfeld eines Vektors nach Komponenten, 
		die einen besseren Funktionswert ergeben.

		Tastet im gegebenen Abstand um die Komponenten und prüft
		an diesen Stellen, ob sich der Funktionswert verbessert. Der optimierte
		Vektor wird zurückgegeben.

		Parameter
		----------
		current_vector : list<double>
			Aktueller Vektor, von dem aus nach Verbesserungen getastet wird

		Returns
		-------
		current_vector : list<double>
			Durch Vorrantasten verbesserter Vektor.
		"""
		old_vector = current_vector.copy()
		current_minimum = self.__eval_function(current_vector.tolist())
		for i in range(self.__dimension):
			#Vorranschreiten in alle Richtungen,
			#d.h. manipulation aller Komponenten des Vektors
			current_vector[i] += self.__delta
			#Exploration in positiver Richtung
			if (self.__eval_function(current_vector.tolist()) < current_minimum):
				current_minimum = self.__eval_function(current_vector.tolist())
			else:
				current_vector[i] -= 2*self.__delta
				#Exploration in negativer Richtung
				if (self.__eval_function(current_vector.tolist()) < current_minimum):
					current_minimum = self.__eval_function(current_vector.tolist())
				else:
					current_vector[i] = old_vector[i]
		return current_vector

	def Optimize(self):
		""" Führt den Optimierungsalgorithmus durch.

		Wählt zufälligen Startpunkt aus. Führt von dort einmalig ein Tasten
		in alle Richtungen durch. Anschließend wird fortlaufend getastet bis
		der beste Funktionswert erreicht ist, anschließend wird die Schritt-
		weite zum Tasten halbiert. 

		Returns
		-------
		psi : list<double>
			Optimierter Vektor gegebener Dimension.
		"""
		psi = numpy.random.uniform(
			self.__lower_bound, self.__upper_bound, self.__dimension)
		while True:
			phi = psi.copy()
			phi = self.__explore(phi.copy())
			if (self.__eval_function(phi.tolist()) < self.__eval_function(psi.tolist())):
				while True:
					#Solange vorranschreiten, wie die Evalierung sich
					# verbessert, d.h. der funktionswert sich verringert
					teta = psi.copy()
					psi = phi.copy()
					phi = phi + self.__alpha * (phi-teta)
					phi = self.__explore(phi.copy())
					if (self.__eval_function(phi.tolist()) >= self.__eval_function(psi.tolist())):
						#Funktionswert hat sich nicht verbessert,
						#aufhören vorranzuschreiten
						break
			else:
				#Schrittgröße halbieren, um Genauigkeit zu verbessern
				self.__delta = self.__delta/2
			if (self.__delta < self.__delta_min):
				#Abbruchkriterium erreicht, schrittgröße nicht weiter halbieren 
				break
		return psi.tolist()
