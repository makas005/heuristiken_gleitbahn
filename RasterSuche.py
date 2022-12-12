class RasterSuche():
    def __init__(self, dimension, lower_bound, upper_bound, eval_function):
        self.__dimension = dimension
        self.__lower_bound = lower_bound
        self.__upper_bound = upper_bound
        self.__grid_size = 10
        self.__eval_function = eval_function
        self.__grid_values = self.__linspace_grid()

    def Optimize(self):
        matrix = self.__create_grid_matrix()
        print(f"Matrix has dimensions {len(matrix)}x{len(matrix[0])}")
        
        optimal_eval_value = -1
        optimal_guesses = [None] * self.__dimension

        for row in matrix:
            current_eval_value = self.__eval_function(row)
            if current_eval_value == -1:
                #error case
                continue
            if optimal_eval_value == -1:
                #first run of loop
                optimal_eval_value = current_eval_value
                optimal_guesses = row.copy()
            elif current_eval_value < optimal_eval_value:
                #better node heights found
                optimal_eval_value = current_eval_value
                optimal_guesses = row.copy()
            
        return optimal_guesses

    def __create_initial_grid_matrix(self):
        grid_matrix = []
        for index in range(len(self.__grid_values)):
            grid_matrix.append([self.__grid_values[index]])
        return grid_matrix

    def __increase_grid_matrix(self, matrix):
        if (len(matrix[0]) == self.__dimension):
            #Matrix has reached final size, it can be returned
            return matrix
        else:
            appended_matrix = []
            for row in matrix:
                for index in range(len(self.__grid_values)):
                    row_to_append = row.copy()
                    row_to_append.append(self.__grid_values[index])
                    appended_matrix.append(row_to_append)
            return self.__increase_grid_matrix(appended_matrix)
    
    def __create_grid_matrix(self):
        matrix = self.__create_initial_grid_matrix()
        return self.__increase_grid_matrix(matrix)
    

    def __linspace_grid(self):
        step = (self.__upper_bound - self.__lower_bound) / float(self.__grid_size-1)
        return [self.__lower_bound + i * step for i in range(self.__grid_size)]
            
