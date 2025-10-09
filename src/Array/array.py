class Array:
    def __init__(self,size):
        self.__array = []
        self.__set_array(size)
        self.__length = size

    def __set_array(self,size):
        if type(size) is not int or size < 1: raise ValueError('size must be an integer')
        for num in range(0,size):
            self.__array.append(0)

    def __get_array(self):
        return self.__array

    def __str__(self):
        return f"{self.__array}"

    def set_element(self,index,value):
        if index < 0 or index >= self.__length:raise IndexError('index out of range')
        self.__array[index] = value

    def get_element(self,index):
        if index < 0 or index >= self.__length: raise IndexError('index out of range')
        return self.__array[index]

    def size(self):
        return self.__length

