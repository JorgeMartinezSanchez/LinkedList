from .Node import Node

class LinkedList:
    def __init__(self):
        self.first: Node = None

    def insert(self, newNode: Node) -> None:
        if self.first is None:
            self.first = newNode
        else:
            current = self.first
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(newNode)

    def delete(self, data) -> bool:
        if self.first is None:
            return False

        if self.first.getData() == data:
            self.first = self.first.getNext()
            return True
        
        current = self.first
        while current.getNext() is not None:
            if current.getNext().getData() == data:
                current.setNext(current.getNext().getNext())
                return True
            current = current.getNext()
        
        return False

    def search(self, data) -> Node | None:
        current = self.first
        while current is not None:
            if current.getData() == data:
                return current
            current = current.getNext()
        return None

    def isEmpty(self) -> bool:
        return self.first is None

    def size(self) -> int:
        count = 0
        current = self.first
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def __str__(self) -> str:
        result = []
        current = self.first
        while current is not None:
            result.append(str(current.getData()))
            current = current.getNext()
        return " -> ".join(result) if result else "Empty list"