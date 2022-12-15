import math
class Segment:
    __delta_height = 0   #Hoehendifferenz
    __length = 0    #Laenge des Segments 
    __initial_velocity = 0 #Anfangsgeschwindigkeit
    __gravity = 9.81  	#Erdbeschleunigung

    def __init__(self, delta_height, length, initial_velocity):
        self.__delta_height = delta_height
        self.__length = length
        self.__initial_velocity = initial_velocity

    def calc_end_velocity(self):
        track_length = math.sqrt(self.__delta_height**2+self.__length**2)
        acceleration = self.__gravity*(self.__delta_height/track_length)
        if acceleration==0:
            time = track_length/self.__initial_velocity
        else:
            root_argument = self.__initial_velocity**2+2*acceleration*track_length
            if(root_argument<0):
                root_argument=0
            time = (-self.__initial_velocity+math.sqrt(root_argument))/acceleration
        velocity_at_endpoint = acceleration*time+self.__initial_velocity
        return velocity_at_endpoint

    def calc_time(self):
        track_length = math.sqrt(self.__delta_height**2+self.__length**2)
        acceleration = self.__gravity*(self.__delta_height/track_length)
        if acceleration==0:
            if self.__initial_velocity==0:
                time = -1
            else:
                time = track_length/self.__initial_velocity   
        else:
            root_argument = self.__initial_velocity**2+2*acceleration*track_length
            if(root_argument<0):
                time = -1
            else:
                time = (-self.__initial_velocity+math.sqrt(root_argument))/acceleration
        return time