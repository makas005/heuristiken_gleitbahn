import importlib, inspect
class IOptimizer:
    def __init__(self, dimension, lower_bound, upper_bound, eval_function, optimizer_name):
        optimizer_module=importlib.import_module("..Optimizer."+optimizer_name)    #import optimizer module
        for name, obj in inspect.getmembers(optimizer_module):            #search for class in optimizer module
            if inspect.isclass(obj):
                cl = obj                                            #get class
        self.optimizer = cl(dimension, lower_bound, upper_bound, eval_function)  #init object of class
    
    def Optimize(self):
        return self.optimizer.Optimize()