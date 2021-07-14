import linkedlist
from linkedlist import LinkedList as ll
from Heap import Heap
from linkedlist import Node
class IslanderQueue(ll,Heap):
    def __init__(self, priority = False):
        ll.__init__(self)
        Heap.__init__(self)
        self.priority = priority
    def Empty(self):
        if self.size() == 0:
            return True
        return False
    def Push(self,data,key = None):
        if (self.priority is True):
            self.Insert(data,key = key)
        else:
            self.Dynamic(data = data)
    def Top(self):
        if (self.priority is True):
            return self.root
        else:
            return self.head.data
    def Pop(self):
        if self.priority is True:
            self.RemoveMax()
        else:
            self.head =self.head.next
if __name__ == '__main__':
    data = IslanderQueue(priority= True)
    data.Push(data={"price":543, "current":"what"},key = "price")
    data.Push(data={"price":0.14, "current":"will"},key = "price")
    print(data._Size(data.root))
    data.Push(data = {"price":0.133,"current":"you"},key = "price")
    # print(data.size())
    # print(data.Top())
    data.PreOrder()