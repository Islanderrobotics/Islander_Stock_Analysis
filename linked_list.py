
class Node:
    '''essentialy this class is the back bone for the linked list '''
    def __init__(self,next = None, price = None, current_percentage = None,
                 overall_percentage = None, symbol = None):
        self.next = next
        self.price = price
        self.current_percentage = current_percentage
        self.overall_percentage = overall_percentage
        self.symbol = symbol

class LinkedList:
    '''this is class will allow for the user the ability to convert
    there data to a linked list'''
    head: Node
    Tail: Node
    def __init__(self):
        self.head = None
        self.tail = None
        self.sizeofLinkedList =0
    def PushFront(self,price:int,current_percentage:float,overall_percentage:float,symbol:str):
        temp = Node(next = self.head,price = price,current_percentage = current_percentage,
                    overall_percentage=overall_percentage, symbol=symbol)
        self.head = temp
        self.sizeofLinkedList+=1
        if (self.sizeofLinkedList==1):
            self.tail = self.head
    def PushBack(self,price:int,current_percentage:float,overall_percentage:float,symbol:str):
        self.tail.next = Node(price=price,current_percentage=current_percentage,overall_percentage=overall_percentage,symbol=symbol)
        self.tail = self.tail.next
        self.sizeofLinkedList+=1
    
    def Dynamic(self,price,current_percentage,overall_percentage,symbol):
        if self.sizeofLinkedList==0:
            self.PushFront(price,current_percentage,overall_percentage,symbol)
        else:
            self.pushBack(price,current_percentage,overall_percentage,symbol)
    def printValues(self)->str:
        print(self.sizeofLinkedList)
        temp: Node = self.head
        size = 0
        while(self.head is not None):
            print(f"{self.head.symbol},{self.head.price},{self.head.overall_percentage}, {self.head.current_percentage}")
            # if (size>=1):
            #     temp.next = self.head
            self.head = self.head.next
        self.head = temp
    def size(self)->str:
        return self.sizeofLinkedList

    def Contains(self,symbol:str)->bool:
        temp: Node = self.head
        while(self.head is not None):
            if (self.head.symbol == symbol):
                return True
            self.head = self.head.next
        self.head = temp
        return False
    def insert(self,price:int,current_percentage:float,overall_percentage:float,symbol:str, index:int):
        if index ==0:
            self.PushFront(price=price,symbol=symbol,current_percentage=current_percentage,overall_percentage=overall_percentage)
            return
        if index >= self.sizeofLinkedList:
            self.PushBack(price=price, symbol=symbol, current_percentage=current_percentage,overall_percentage=overall_percentage)
        temp :Node = self.head
        curr_index = 0
        while(curr_index != index-1):
            temp = temp.next
            curr_index+=1
        new_node: Node = Node(next=temp.next, price=price,symbol=symbol,current_percentage=current_percentage,overall_percentage=overall_percentage)
        temp.next = new_node
        self.sizeofLinkedList+=1
    def delete(self,symbol):
        current:Node = self.head
        previouse:Node = None

        if (current.symbol == symbol):
            previouse = current
            self.head = current.next
            del previouse
            self.sizeofLinkedList=-1
        else:
            while(current.symbol != symbol and current is not None):
                previouse = current
                current = current.next
        if(current):
            if (current ==self.tail):
                self.tail = previouse
            previouse.next = current.next
            del current
            self.sizeofLinkedList-=1
data = LinkedList()
if __name__ == "__main__":
    data.PushFront(price=123, symbol="what",current_percentage=100, overall_percentage = 20)
    data.printValues()
    data.PushBack(price = 430, symbol="will",current_percentage=300, overall_percentage=432)
    data.printValues()
    data.Dynamic(price = 200,symbol="you",current_percentage=54,overall_percentage=45)
    data.printValues()
    data.insert(price = 200,symbol="do",current_percentage=54,overall_percentage=45,index=2)
    data.printValues()
    data.delete("do")
    data.printValues()