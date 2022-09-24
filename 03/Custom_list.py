from functools import reduce
import copy

class Custom_list(list):
    def __sub__(self, obj, reverse=False):
        buf_self = copy.copy(self)
        buf_obj = copy.copy(obj)
        if reverse: buf_self, buf_obj = buf_obj, buf_self
        buf_min = min(buf_self, buf_obj, key=len)
        buf_len = max(len(buf_self), len(buf_obj))
        Custom_list.refill(buf_min, buf_len)
        result = map(lambda x, y : x-y, buf_self, buf_obj)
        return Custom_list(result)

    def __rsub__(self, obj):
        return self.__sub__(obj, True)

    def __add__(self, obj):
        buf_self = copy.copy(self)
        buf_obj = copy.copy(obj)
        buf_min = min(buf_self, buf_obj, key=len)
        buf_len = max(len(buf_self), len(buf_obj))
        Custom_list.refill(buf_min, buf_len)
        result = map(lambda x, y : x+y, buf_self, buf_obj)
        return Custom_list(result)

    def __radd__(self, obj):
        return self.__add__(obj)

    @staticmethod
    def list_to_int(obj):
        return reduce(lambda x, y: x+y, obj, 0)

    @staticmethod
    def refill(obj, data_len):
        while len(obj) != data_len:
            obj.append(0)

    def __lt__(self, other): #x < y
        return Custom_list.list_to_int(self) < Custom_list.list_to_int(other)

    def __le__(self, other): # x ≤ y
        return Custom_list.list_to_int(self) <= Custom_list.list_to_int(other)

    def __eq__(self, other): # x == y 
        return Custom_list.list_to_int(self) == Custom_list.list_to_int(other)

    def __ne__(self, other): # x != y 
        return Custom_list.list_to_int(self) != Custom_list.list_to_int(other)

    def __gt__(self, other):# x > y 
        return Custom_list.list_to_int(self) > Custom_list.list_to_int(other)

    def __ge__(self, other): # x ≥ y
        return Custom_list.list_to_int(self) >= Custom_list.list_to_int(other)
    
    def __str__(self):
        return f"{[x for x in self]}, {Custom_list.list_to_int(self)}"

