from typing import Self

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node = None
    
    def getData(self):
        return self.data
    
    def setData(self, newData) -> None:
        self.data = newData

    def getNext(self) -> Self:
        return self.next
    
    def setNext(self, newNext) -> None:
        self.next = newNext