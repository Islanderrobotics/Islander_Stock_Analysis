from node import Node
from tree import Tree
class Heap(Tree):
    '''this is where we will build and actual heap'''
    def __init__(self,dictionary =False):
        Tree.__init__(self)
        self.dictionary = dictionary

    def _Insert(self,data,root):
        if (root is None):
            return Node(data = data)
        if (data>root.data):
            temp = root.data
            root.data = data
            data  = temp

        if(self._IsFull(root) and self._Size(root.left) == self._Size(root.right) or self._IsFull(root.left) is False):
            root.left = self._Insert(data,root.left)
        else:
            root.right = self._Insert(data,root.right)
        return root
    def _InsertDict(self,data,root,key):
        if (root is None):
            return Node(data = data)
        if (data[key]>root.data[key]):
            temp = root.data
            root.data = data
            data  = temp

        if(self._IsFull(root) and self._Size(root.left) == self._Size(root.right) or self._IsFull(root.left) is False):
            root.left = self._InsertDict(data,root.left,key)
        else:
            root.right = self._InsertDict(data,root.right,key)
        return root

    def _Delete(self,root):
        if (root is None):
            return
        self._Delete(root.left)
        self._Delete(root.right)
        del root
    def _Search(self,root,data):
        if (root is None):
            return False
        if (root.data == data):
            return True
        found = self._Search(root.left,data)
        if (found):
            return True
        return self._Search(root.right,data)
    def _SearchDict(self,root,data,key):
        if (root is None):
            return False
        if (root.data[key] == data[key]):
            return True
        found = self._SearchDict(root.left,data,key)
        if (found):
            return True
        return self._SearchDict(root.right,data,key)
    def _MaxHeapify(self,root):
        if root is None:
            return None
        if (root.left is not None):
            # print("max_left")
            if (root.left.data>root.data):
                # print("max left _1")
                temp_left = root.left.left
                temp_right = root.left.right
                root.left.right = root.right
                root.left.left = root
                root = root.left

                root.left.left = temp_left
                root.left.right = temp_right
            root.left = self._MaxHeapify(root.left)

        if (root.right is not None):
            # print("max right")
            if (root.right.data>root.data):
                # print("max right 1")
                temp_left = root.right.left
                temp_right = root.right.right

                root.right.left = root.left
                root.right.right = root

                root = root.right

                root.right.left = temp_left
                root.right.right = temp_right
            root.right = self._MaxHeapify(root.right)
        return root
    def _MaxHeapifyDict(self,root,key):
        if root is None:
            return None
        if (root.left is not None):
            if (root.left.data[key]>root.data[key]):
                temp_left = root.left.left
                temp_right = root.left.right
                root.left.right = root.right
                root.left.left = root
                root = root.left

                root.left.left = temp_left
                root.left.right = temp_right
            root.left = self._MaxHeapifyDict(root.left,key)

        if (root.right is not None):

            if (root.right.data[key]>root.data[key]):
                # print("max_right")
                temp_left = root.right.left
                temp_right = root.right.right

                root.right.left = root.left
                root.right.right = root

                root = root.right

                root.right.left = temp_left
                root.right.right = temp_right
            root.right = self._MaxHeapifyDict(root.right,key)
        return root
    def _FindLast(self,root,index,node_count):
        if root is None or index>= node_count:
            return None
        if (2*index+1 == node_count-1):

            temp = root.left
            root.left = None
            return temp
        if (2*index+2 == node_count-1):

            temp = root.right
            root.right = None
            return temp
        left_results = self._FindLast(root.left,2*index+1, node_count)
        if (left_results is not None):
            return left_results
        return self._FindLast(root.right,2*index+2,node_count)
    def _RemoveLast(self, root):
        last_node = self._FindLast(self.root,0,self._Size(self.root))
        root = last_node
        del last_node
    def _DeleteElement(self,data,root):
        if (root is None):
            return
        if (root.data == data):
            last_node = self._FindLast(self.root,0,self._Size(self.root))
            root.data = last_node.data
            del last_node
            return
        self._DeleteElement(data,root.left)
        self._DeleteElement(data,root.right)
    def _DeleteElementDict(self,data,root,key):
        if (root is None):
            return
        if (root.data[key] == data[key]):
            last_node = self._FindLast(self.root,0,self._Size(self.root))
            root.data = last_node.data
            del last_node
            return
        self._DeleteElementDict(data,root.left,key)
        self._DeleteElementDict(data,root.right,key)
    def _RemoveMax(self,root):
        last_node = self._FindLeftMost(self.root)
        self.top = root.data
        root.data = last_node.data
        del last_node
    def _FindLeftMost(self,root):
        if (root.left is None):
            temp = root
            # print(root is None)
            root = None
            return temp
        return self._FindLeftMost(root.left)
    def ConvertToList(self):
        self.sorted_data = []
        self.sorted_data.append(self.root.data)
        self.RemoveMax(key="price")
        self.sorted_data.append(self.root.data)
        self.RemoveMax(key="price")
        for i in range(self._Size(self.root)):

            self.sorted_data.append(self.root.data)
            self.RemoveMax(key="price")
            if (self.sorted_data[-1] == self.sorted_data[-2] ):
                self.sorted_data.pop(-1)

    '''this is where all of the above functions will get called'''
    def DeleteQueue(self):
        self._Delete(self.root)
    def Insert(self,data,key = None):
        if (isinstance(data,dict)):
            self.root = self._InsertDict(data, self.root,key)
        else:
            self.root = self._Insert(data,self.root)
        self.dictionary = isinstance(data,dict)

    def Search(self,data,key = None):
        if (self.dictionary):
            return self._SearchDict(data = data, root = self.root,key = key)
        else:
            return self._Search(data= data, root = self.root)
    def RemoveMax(self, key = None):
        self._RemoveMax(self.root)
        if (self.root):
            if (self.dictionary):
                self.root = self._MaxHeapifyDict(self.root,key = key)
            else:
                self.root = self._MaxHeapify(self.root)
    def DeleteElement(self,data,key = None):
        if (self.dictionary):
            self._DeleteElementDict(data=data)
        else:
            self._DeleteElement(data= data, root = self.root)
    def FindLast(self):
        temp = self._FindLast(self.root, 0, self._Size(self.root))
        print(temp.data)
    def Heapify(self, key = None):
        if (self.dictionary):
            self._MaxHeapifyDict(root = self.root, key = key)
        else:
            self._MaxHeapify(root = self.root)


    def Convert(self, type="queue"):
        self.Heapify(key="price")
        # temp = self.root
        # if (type=="queue"):
        #     self.ConvertToQueue()
        #  elif (type == "list"):
        self.ConvertToList()
        # self.root = temp
if __name__ == "__main__":
    data = Heap()
    data.Insert({'price': 9.73, 'symbols': 'ADRA', 'percentage': 0.12},key = "price")
    data.Insert({'price': 7.57, 'symbols': 'APT', 'percentage': 0.49},key = "price")
    data.Insert({'price': 4.0, 'symbols': 'BTG', 'percentage': 0.05},key = "price")
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key = "price")
    data.Insert({'price': 9.73, 'symbols': 'ADRA', 'percentage': 0.12}, key="price")
    data.Insert({'price': 7.57, 'symbols': 'APT', 'percentage': 0.49}, key="price")
    data.Insert({'price': 4.0, 'symbols': 'BTG', 'percentage': 0.05}, key="price")
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")
    data.Insert({'price': 9.88, 'symbols': 'APT', 'percentage': 0.82, 'overall_percentage': 9.05}, key="price")
    data.Insert({'price': .22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")
    data.Insert({'price': 4.4, 'symbols': 'AWX', 'percentage': 0.02, 'overall_percentage': 0.46}, key="price")
    data.Insert({'price': 2.76, 'symbols': 'AMS', 'percentage': 0.05, 'overall_percentage': 1.85}, key="price")
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")
    # print(f"what{data._IsFull(data.root)}")
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")
    # print("10")
    # print(data._Size(data.root.left) == data._Size(data.root.right))
    # print(f"what{data._IsFull(data.root)}")
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")
    # print("11")
    # print(data._Size(data.root.left) == data._Size(data.root.right))
    # print(f"what{data._IsFull(data.root)}")
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")  # 10 11 18 19
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")  # 22
    # data.Insert(5);
    # data.Insert(3);
    # data.Insert(7);
    # data.Insert(2);
    # data.Insert(4);
    # data.Insert(6);
    # data.Insert(8);
    # data.PreOrder()
    # print(data.FindLast())
    data.Convert(type = "list")
    for  i in data.sorted_data:
        print(i)        
    # data.PostOrder()
    # # print(data.Height())
    # print(data.IsComplete())
    # # print(data.Search(101, key = "price"))
    # print(data.IsFull())
    # data.RemoveMax()
    # data.RemoveMax()
    # # data.DeleteElement(8)
    # data.PostOrder()
    # # {'price': 4.0, 'symbols': 'BTG', 'percentage': 0.05}
    # # {'price': 4.1, 'symbols': 'AWX', 'percentage': 0.09}
