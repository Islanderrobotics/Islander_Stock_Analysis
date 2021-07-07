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
    def Size(self):
        return self.size_
    def contains(self, symbol):
        temp = self.head
        while(temp is not None):
            if (temp.symbol == symbol):
                return True
            temp = temp.next
        return False

    def insert(self, price: int, current_percentage: float, overall_percentage: float, symbol: str, index: int):
        if index == 0:
            self.PushFront(price=price, symbol=symbol, current_percentage=current_percentage,
                           overall_percentage=overall_percentage)
            return
        if index >= self.size_:
            self.PushBack(price=price, symbol=symbol, current_percentage=current_percentage,
                          overall_percentage=overall_percentage)
        temp: Node = self.head
        curr_index = 0
        while (curr_index != index - 1):
            temp = temp.next
            curr_index += 1
        new_node: Node = Node(next=temp.next, price=price, symbol=symbol, current_percentage=current_percentage,
                              overall_percentage=overall_percentage)
        temp.next = new_node
        self.size_ += 1

    def delete(self, symbol):
        current: Node = self.head
        previouse: Node = None

        if (current.symbol == symbol):
            previouse = current
            self.head = current.next
            del previouse
            self.size_ = -1
        else:
            while (current.symbol != symbol and current is not None):
                previouse = current
                current = current.next
        if (current):
            if (current == self.tail):
                self.tail = previouse
            previouse.next = current.next
            del current
            self.size_ -= 1

if __name__ == "__main__":
    data = LinkedList()
    data.PushFront(price=123, symbol="what", current_percentage=100, overall_percentage=20)
    data.PrintValues()
    data.PushBack(price=430, symbol="will", current_percentage=300, overall_percentage=432)
    data.PrintValues()
    data.Dynamic(price=200, symbol="you", current_percentage=54, overall_percentage=45)
    data.PrintValues()
    print("this is the new stuff")
    data.insert(price=200, symbol="do", current_percentage=54, overall_percentage=45, index=2)
    data.PrintValues()
    data.delete("do")
    data.PrintValues()
    print(data.contains("do"))