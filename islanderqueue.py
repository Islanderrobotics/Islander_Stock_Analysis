import linkedlist
from linkedlist import LinkedList as ll
from linkedlist import Node
class IslanderQueue(ll):
    def __init__(self, priority = False):
        ll.__init__(self)
        self.priority = priority
    def Empty(self):
        if self.size() == 0:
            return True
        return False
    def Push(self,data,key = None):
        if (self.priority):
            self.Priority(index = data,key = key)
        else:
            self.Dynamic(data = data)
    def Top(self, pop=False):
        data = self.head.data
        if (pop is True):
            self.head = self.head.next
        return data
    def Pop(self):
        self.head =self.head.next
    def Priority(self, index, key=None):
        if self.sizeofLinkedList == 0:
            self.PushFront(index)
            return
        temp:Node = self.head
        if (isinstance(self.head.data, dict) is False):

            while (temp is not None and temp.data < index):
                temp = temp.next
        else:
            print("yes")
            while (temp is not None and temp.data[key] < index[key]):
                temp = temp.next
        if (temp):
            new_node: Node = Node(next=temp.next, data=index)
            temp.next = new_node
        else:
            self.PushBack(data = index)
        self.sizeofLinkedList += 1

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