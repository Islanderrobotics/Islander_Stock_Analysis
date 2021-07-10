# import Percentage as Percentage

from linked_list import LinkedList
class Queue:
    def __init__(self):
        self.queue = LinkedList()
    def empty(self):
        if self.queue.sizeofLinkedList == 0:
            return False
        return True
    def size(self):
        return self.queue.sizeofLinkedList
    def push(self,data):
        self.queue.Dynamic(data = data)
        self.head = self.queue.head
    def top(self, pop = False):
        data = self.head.data
        if (pop):
            self.head = self.head.next
        return data
    def pop(self):
        self.head =self.head.next


if __name__ == "__main__":
    data = Queue()
    print(data.empty())
    print(data.size())
    data.push(data = {"price":832, "symbol":"what", "Percentage":43})
    print(data.size())
    data.push(data = {"price":123, "symbol":"will", "current_percentage":100, "overall_percentage":20})
    print(data.size())
    data.push(data = {"price":123, "symbol":"you", "current_percentage":100, "overall_percentage":20})
    print(data.size())
    print(data.top())
    bob = data.head
    while(data.queue.head is not None):
        print(data.queue.head.data)
        data.queue.head = data.queue.head.next
    data.head = bob
    data.pop()
    while (data.head is not None):
        print(data.head.data)
        data.head = data.head.next