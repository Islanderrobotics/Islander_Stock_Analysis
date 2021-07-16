


class Node:
    '''essentialy this class is the back bone for the linked list '''

    def __init__(self, next=None, data=None):
        self.next = next
        self.data = data


class LinkedList:
    '''this is class will allow for the user the ability to convert
    there data to a linked list'''
    head: Node
    Tail: Node

    def __init__(self):
        self.head = None
        self.tail = None
        self.sizeofLinkedList = 0

    def PushFront(self, data):
        temp = Node(next=self.head, data=data)
        self.head = temp
        self.sizeofLinkedList += 1
        if (self.sizeofLinkedList == 1):
            self.tail = self.head

    def PushBack(self, data):
        self.tail.next = Node(data=data)
        self.tail = self.tail.next
        self.sizeofLinkedList += 1

    def Dynamic(self, data):
        if self.sizeofLinkedList == 0:
            self.PushFront(data)
        else:
            self.PushBack(data)

    def printValues(self) -> str:
        temp: Node = self.head
        size = 0
        while (self.head is not None):
            if (isinstance(self.head.data, dict) is False):
                print("yes")
                print(f"{self.head.data}")
            else:
                print(f"{self.head.data}")
            # if (size>=1):
            #     temp.next = self.head
            self.head = self.head.next
        self.head = temp

    def size(self) -> int:
        return self.sizeofLinkedList

    def Contains(self, symbol: str) -> bool:
        temp: Node = self.head
        while (self.head is not None):
            if (self.head.symbol == symbol):
                return True
            self.head = self.head.next
        self.head = temp
        return False

    def insert(self, data, index):
        if index == 0:
            self.PushFront(data)
            return
        if index >= self.sizeofLinkedList:
            self.PushBack(data)
        temp: Node = self.head
        curr_index = 0
        while (curr_index != index - 1):
            temp = temp.next
            curr_index += 1
        new_node: Node = Node(next=temp.next, data=data)
        temp.next = new_node
        self.sizeofLinkedList += 1

    def deleteReg(self, symbol):
        current: Node = self.head
        previouse: Node = None

        if (current.data == symbol):
            previouse = current
            self.head = current.next
            del previouse
            self.sizeofLinkedList = -1
        else:
            while (current.data != symbol and current is not None):
                previouse = current
                current = current.next
        if (current):
            if (current == self.tail):
                self.tail = previouse
            previouse.next = current.next
            del current
            self.sizeofLinkedList -= 1

    def deletedict(self, key, data):
        current: Node = self.head
        previouse: Node = None

        if (current.data[key] == data):
            previouse = current
            self.head = current.next
            del previouse
            self.sizeofLinkedList = -1
        else:
            while (current.data[key] != data and current is not None):
                previouse = current
                current = current.next
        if (current):
            if (current == self.tail):
                self.tail = previouse
            previouse.next = current.next
            del current
            self.sizeofLinkedList -= 1

    def delete(self, data, dict=False, key=""):
        if (dict is False):
            self.deleteReg(data)
        else:
            self.deletedict(key=key, data=data)
if __name__ == "__main__":
    data = LinkedList()
    data.PushFront(data={"price": 123, "current percentage": 43})
    data.PushFront(data={"price": 89, "current percentage": 79})
    data.PushBack(data={"price": 54, "current percentage": 89})
    data.Priority(index={"price": 874, "current": 42},key = "price")
    # data.delete(data=89, dict=True, key="current percentage")
    data.printValues()