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
        if a==0:
            t = s/self.__v_initial
        else:
            t = (-self.__v_initial+math.sqrt(self.__v_initial**2+2*a*s))/(a)
        v_end = a*t+self.__v_initial
        return v_end

    def CalcT(self):
        s = math.sqrt(self.__delta_h**2+self.__length**2)
        a = self.__g*(self.__delta_h/s)
        if a==0:
            #No acceleration
            if self.__v_initial==0:
                #If no acceleration and no initial speed, then fail
                t = -1
            else:
                #Movement without acceleration
                t = s/self.__v_initial   
        else:
            root_argument = self.__v_initial**2+2*a*s
            if root_argument < 0:
                #Error case: negative root argument means acceleration is not great enough to climb to top of segment
                t = -1
            else:
                #Formula to compute accelerated movement
                t = (-self.__v_initial+math.sqrt(root_argument))/(a)
        return t
    
    def GetDeltaH(self):
        return self.__delta_h