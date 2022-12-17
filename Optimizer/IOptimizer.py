import importlib, inspect
class IOptimizer:
    """Interface für alle Optimizer-Klassen
    
    Methoden
    --------
    Optimize()
        Führt den Optimierungsalgorithmus aus, optimiert immer auf niedrigste Werte

    """


    def __init__(self, dimension, lower_bound, upper_bound, eval_function, optimizer_name):
        """
        Parameter
        ---------
        dimension : unsigned int
            Anzahl der Dimensionen in denen optimiert werden soll
            
        lower_bound : int
            Untere Schranke für Werte, die vom Optimierungsalgorithmus ausgegeben werden
            
        upper_bound : int 
            Obere Schranke für Werte, die vom Optimierungsalgorithmus ausgegeben werden
            
        eval_function : function
            Evaluiert Funktionswert des Testvektors anhand des aktuellen getesteten Parameters.
            Muss eine Liste von double akzeptieren und dounble zurückgeben
        
        optimizer_name : string
            Name des Optimierungsalgorithmus entsprechend des Dateinamens
        """


        optimizer_module=importlib.import_module("Optimizer."+optimizer_name)    #import optimizer module
        for name, obj in inspect.getmembers(optimizer_module):            #search for class in optimizer module
            if inspect.isclass(obj):
                cl = obj                                            #get class
        self.optimizer = cl(dimension, lower_bound, upper_bound, eval_function)  #init object of class
    
    def Optimize(self):
        """ Führt Optimierungsalgorithmus aus
        
        Führt den im Konstruktor gewählten Optimierungsalgorithmus aus
        """

        
        return self.optimizer.Optimize()