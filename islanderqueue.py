import linkedlist
from linkedlist import LinkedList as ll
from Heap import Heap
from linkedlist import Node
class IslanderQueue(ll,Heap):
    def __init__(self, priority = False):
        ll.__init__(self)
        Heap.__init__(self)
        self.priority = priority
        self.count = 0
    def Empty(self):
        if self.size() == 0:
            return True
        return False
    def Size(self):
        if (self.priority):
            return self._Size(self.root)
        else:
            return self.size()
    def Push(self,data,key = None):
        if (self.priority is True):
            self.count += 1
            self.Insert(data,key = key)
        else:
            self.Dynamic(data = data)
    def Top(self):
        if (self.priority is True):
            return self.root
        else:
            return self.head.data
    def Pop(self,key = None):
        if self.priority is True:
            self.RemoveMax(key = key)
        else:
            self.head =self.head.next
    def ConvertToList(self):
        self.sorted_data = []
        while (True):
            try:
                self.sorted_data.append(self.root.data)
                self.RemoveMax(key = "price")
            except AttributeError:
                break
    def ConvertToQueue(self):
        while (True):
            try:
                self.Dynamic(data=self.root.data)
                self.RemoveMax(key="price")
            except AttributeError:
                break
            self.sorted_data = self.head
    def Convert(self,type ="queue"):
        self.Heapify(key = "price")
        temp = self.root
        if (type=="queue"):
            self.ConvertToQueue()
        elif (type == "list"):
            self.ConvertToList()
            self.root = temp    
if __name__ == '__main__':
    data = IslanderQueue(priority= True)
    data.Push(data={"price":543, "current":"what"},key = "price")
    data.Push(data={"price":0.14, "current":"will"},key = "price")
    print(data._Size(data.root))
    data.Push(data = {"price":0.133,"current":"you"},key = "price")
    data.Heapify(key="price")
    while (data.root is not None):
        data.Dynamic(data.root.data)
        if (data.root.left is not None or data.root.right is not None):
            data.RemoveMax(key="price")
        if (data.root.left is None and data.root.right is None):
            data.Dynamic(data.root.data)
            break

    while(data.head is not None):
        print(data.head.data)
        data.head = data.head.next
