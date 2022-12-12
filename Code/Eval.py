class Eval: 
    def __init__(self, init_h, seg_length):
        self.__init_h = init_h
        self.__seg_length = seg_length

    def eval_func(self, node_arr):
        node_arr.append(0)
        t = 0
        h = self.__init_h
        l = self.__seg_length
        v_curr = 0
        for i in range(len(node_arr)):
            s = Segment(h-node_arr[i], l, v_curr)
            h = node_arr[i]
            t_seg = s.CalcT()
            if(t_seg!=-1):
                v_curr = s.CalcVEnd()
                t += t_seg
            else:
                break
        node_arr.pop()
        if(t_seg==-1):
            return -1
        else:
            return t