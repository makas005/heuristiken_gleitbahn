from Code.Segment import Segment
class Eval: 
    def __init__(self, initial_height, segment_length):
        self.__initial_height = initial_height
        self.__segment_length = segment_length

    def evaluate(self, nodes):
        nodes.append(0)  #Endppunkt der Kurve hinzufügen
        total_time = 0
        height = self.__initial_height
        length = self.__segment_length
        current_velocity = 0
        for i in range(len(nodes)):
            segment = Segment(height-nodes[i], length, current_velocity)
            height = nodes[i]
            segment_time = segment.calc_time()
            if(segment_time!=-1):
                current_velocity = segment.calc_end_velocity()
                total_time += segment_time
            else:
                break
        nodes.pop() #Endpunkt wieder gelöscht
        if(segment_time==-1):
            #Fehlerfall
            return -1
        else:
            return total_time