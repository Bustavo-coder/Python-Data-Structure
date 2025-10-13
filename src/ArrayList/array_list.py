from idlelib.configdialog import changes

from src.Array.array import Array
class ArrayList:
    def __init__(self,length = 10):
        self.__size = 0
        self.__element = Array(length)

    def is_empty(self):
        return self.__size == 0

    def append(self,element):
        self.__element.set_element(self.__size, element)
        self.__size += 1

        if self.__is_full():
            self.__increase_size()

    def size(self):
        return self.__size

    def clear(self):
        for count in range(0, self.__size):
            self.__element.set_element(count, 0)
        self.__size = 0

    def pop(self):
        if self.is_empty(): raise IndexError('Cannot pop from an empty list')
        popped = self.__element.get_element(self.__size - 1)
        self.__size -= 1
        self.__element.set_element(self.__size,0 )
        return popped

    def contains(self,element):
        self.__raise()
        for count in range(0,self.__size):
            if self.__element.get_element(count) == element:
                return True
        else : return False

    def index(self,element):
        self.__raise()
        for count in range(0,self.__size):
            if self.__element.get_element(count) == element:
                return count
        else : return -1

    def remove(self,element):
        if not self.contains(element):
            raise ValueError("value not available")
        count = self.index(element)
        self.__element.set_element(count,0)
        return True

    def insert(self,index,element):
        if index >= self.__size or index < 0: raise IndexError("index out of range")
        self.__change_position(index,element)
        return True




    #Helper Methods
    def __increase_size(self):
        new_list = Array(self.__size * 2)
        for count in range(0,self.__size):
            new_list.set_element(count,self.__element.get_element(count))
        self.__element = new_list

    def __is_full(self):
        return self.__size == self.__element.size()

    def __raise(self):
        if self.is_empty():
            raise IndexError('List is Empty')

    def __sort(self):
        change = None
        box = self.__element

        for element in range(0,self.__size):
            for count in range(element,self.__size):
                if box.get_element(element) == 0 :
                    change = box.get_element(element)
                    box.set_element(element,box.get_element(count))
                    box.set_element(count,change)

    def __change_position(self,index,element):
        box = self.__element
        counter = self.__size - 1
        self.__size += 1
        for count in reversed(range(index, self.__size)):
            box.set_element(count, box.get_element(counter))
            counter -= 1
            if count == index: box.set_element(2, element)