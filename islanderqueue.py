
from linkedlist import LinkedList as ll
class IslanderQueue(ll):
    def __init__(self):
        ll.__init__(self)
        
    def Empty(self):
        if self.size() == 0:
            return True
        return False
    def Push(self,data,key = None):
        self.Dynamic(data = data)
    def Top(self, pop=False):
        data = self.head.data
        if (pop is True):
            self.head = self.head.next
        return data
    def Pop(self):
        self.head =self.head.next

if __name__ == '__main__':
    data = IslanderQueue(priority= True)
    print(data.Empty())
    print(data.size())
    # data.Push(data = 128)
    data.Push(data=0.832)
    print(data.size())
    data.Push(data=0.123)
    print(data.size())
    data.Push(0.133)
    print(data.size())
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
