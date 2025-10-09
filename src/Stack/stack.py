from src.Array.array import Array
class Stack:
    def __init__(self,range = 5):
        self.__size = 0
        self.__element = Array(range)
    def is_empty(self):
        return self.__size == 0

    def push(self,element):
        if(self.__is_full()) : raise IndexError("Stack is full")
        self.__element.set_element(self.__size,element)
        self.__size += 1
        return element

    def pop(self):
        if self.is_empty(): raise IndexError("Stack is empty")
        self.__size -= 1
        return self.__element.get_element(self.__size)

    def __is_full(self):
        return self.__size == self.__element.size()

    def peek(self):
        if self.is_empty(): raise IndexError("Stack is empty")
        return self.__element.get_element(self.__size - 1)

    def size(self):
        return self.__size

    def search(self,element):
        if self.is_empty(): raise IndexError("Stack is empty")
        for elements in range(0,self.__size):
            if self.__element.get_element(elements) == element:
                return elements + 1
        else: return -1