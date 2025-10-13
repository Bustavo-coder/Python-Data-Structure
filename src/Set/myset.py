from src.ArrayList.array_list import ArrayList

class Set(ArrayList):
    def __init__(self, size=10):
        super().__init__(size)
    def add(self,element):
        if self.contains(element):
            raise ValueError("Cannot contain Duplicate element")
        self.append(element)