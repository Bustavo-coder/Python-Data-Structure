from src.Array.array import Array
class Queue:
    def __init__(self,size = 10):
        self.__count = 0
        self.__size = size
        self.__elements = Array(self.__size)
        self.__top = 0

    def is_empty(self):
        return self.__count == 0

    def add(self,element):
        if self.__is_full(): raise Exception('Queue is full')
        if element is None:raise TypeError("Invalid Type None Not Accepted")
        self.__elements.set_element(self.__count,element)
        self.__count += 1

    def element(self):
        if self.is_empty(): raise Exception("Queue is Empty")
        return self.__elements.get_element(self.__top)

    def remove(self):
        if self.is_empty(): raise Exception("Queue is Empty")
        element = self.__elements.get_element(self.__top)
        self.__top += 1;self.__count -= 1
        return element

    def __is_full(self):
        return self.__count >= self.__size
