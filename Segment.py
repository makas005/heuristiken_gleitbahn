import math
class Segment:
    __delta_h = 0   #Hoehendifferenz
    __length = 0    #Laenge des Segments
    __v_initial = 0 #Anfangsgeschwindigkeit
    __g = 9.81  	#Fallbeschleunigung

    def __init__(self, delta_h, length, v_initial):
        self.__delta_h = delta_h
        self.__length = length
        self.__v_initial = v_initial

    def CalcVEnd(self):
        s = math.sqrt(self.__delta_h**2+self.__length**2)
        a = self.__g*(self.__delta_h/s)
        t = (-self.__v_initial+math.sqrt(self.__v_initial**2+2*a*s))/a
        v_end = 0.5*a*(t**2)+self.__v_initial
        return v_end

    def CalcT(self):
        s = math.sqrt(self.__delta_h**2+self.__length**2)
        a = self.__g*(self.__delta_h/s)
        t = (-self.__v_initial+math.sqrt(self.__v_initial**2+2*a*s))/a
        return t
    
    def GetDeltaH(self):
        return self.__delta_h