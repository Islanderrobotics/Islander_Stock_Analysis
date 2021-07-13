from linkedlist import LinkedList as ll

class IslanderQueue:
    def __init__(self):
        self.queue = ll()
    def Empty(self):
        if self.queue.size() == 0:
            return True
        return False
    def Size(self):
        return self.queue.size()
    def Push(self,data):
        self.queue.Dynamic(data = data)
        self.head = self.queue.head
    def Top(self, pop=False):
        data = self.head.data
        if (pop is True):
            self.head = self.head.next
        return data
    def Pop(self):
        self.head =self.head.next

if __name__ == '__main__':
    data = Queue()
    print(data.Empty())
    print(data.Size())
    data.Push(data = 128)
    # data.Push(data={"price": 832, "symbol": "what", "Percentage": 43})
    # print(data.Size())
    # data.Push(data={"price": 123, "symbol": "will", "current_percentage": 100, "overall_percentage": 20})
    # print(data.Size())
    # data.Push(data={"price": 123, "symbol": "you", "current_percentage": 100, "overall_percentage": 20})
    # print(data.Size())
    # print(data.Top())
    bob = data.head
    while (data.head is not None):
        print(data.head.data)
        data.head = data.head.next
    data.head = bob
    # data.Pop()
    # while (data.head is not None):
    #     print(data.head.data)
    #     data.head = data.head.next