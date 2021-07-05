class Node:
    '''this is where the data of the linked list will be'''
    def __init__(self,next = None, price = None,current_percentage = None,overall_percentage = None,symbol = None):
        self.next = next
        self.price = price
        self.current_percentage = current_percentage
        self.overall_percentage = overall_percentage
        self.symbol = symbol

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size_ = 0
    def PushFront(self,price,current_percentage,overall_percentage,symbol):
        temp = Node(next = self.head, price = price,current_percentage = current_percentage,overall_percentage = overall_percentage,
                    symbol = symbol)
        self.head = temp
        self.size_+=1

        if(self.size_==1):
            self.tail = self.head
    def PushBack(self,price,current_percentage,overall_percentage,symbol):
        self.tail.next = Node(price = price,current_percentage = current_percentage,overall_percentage = overall_percentage,
                              symbol = symbol)
        self.tail = self.tail.next
        self.size_+=1
    def Dynamic(self,price,current_percentage,overall_percentage,symbol):
        if self.size_ == 0:
            self.PushFront(price = price,current_percentage = current_percentage,overall_percentage = overall_percentage,
                           symbol = symbol)
        else:
            self.PushBack(price = price,current_percentage = current_percentage,overall_percentage = overall_percentage,symbol=symbol)
    def PrintValues(self):
        temp = self.head
        while(temp is not None):
            print(f"{temp.symbol}, {temp.price},{temp.current_percentage},{temp.overall_percentage}")
            temp = temp.next

if __name__ == "__main__":
    data = LinkedList()
    data.PushFront(123,43, 56,"what")
    data.PrintValues()
    print("the new list is ")
    data.PushBack(432,6543,6,"will")
    data.PrintValues()
    data.Dynamic(725,635,25,"you")
    data.PrintValues()