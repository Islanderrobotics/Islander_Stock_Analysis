


class HeapNode(object):
    '''due to the way that heaps work we will need a new Node class'''
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

class Heap(object):
    '''this is where we will build and actual heap'''
    def __init__(self,dictionary =False):
        self.root = None
        self.dictionary = dictionary

    def _Insert(self,data,root):
        if (root is None):
            return HeapNode(data = data)
        if (data>root.data):
            temp = root.data
            root.data = data
            data  = temp
        # print(self._Size(root.left) == self._Size(root.right))
        # print(f"what{self._IsFull(root)}")
        if(self._IsFull(root) and self._Size(root.left) == self._Size(root.right) or self._IsFull(root.left)is not True):
            root.left = self._Insert(data,root.left)
        else:
            root.right = self._Insert(data,root.right)
        return root
    def _InsertDict(self,data,root,key):
        if (root is None):
            return HeapNode(data = data)
        if (data[key]>root.data[key]):
            temp = root.data
            root.data = data
            data  = temp

        if(self._IsFull(root) and self._Size(root.left) == self._Size(root.right) or self._IsFull(root.left) is False):
            root.left = self._InsertDict(data,root.left,key)
        else:
            root.right = self._InsertDict(data,root.right,key)
        return root
    def _IsFull(self, root):
        if root is None:
            return False
        if (root.left is None and root.right is None):
            return True
        if (root.left is not None and root.right is not None):
            return self._IsFull(root.left) and self._IsFull(root.right)
        return False

    def _Height(self, root):
        if (root is None):
            return -1
        left = self._Height(root.left)
        right = self._Height(root.right)
        if(left>right):
            return(left+1)
        else:
            return(right+1)

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
    def _IsComplete(self,root, index,node_count):
        if root is None:
            return  True
        if (index>=node_count):
            return False

        left_completed = self._IsComplete(root.left,2*index+1,node_count)
        right_completed = self._IsComplete(root.right,2*index+2,node_count)
        return left_completed and right_completed
    def _Size(self,root):
        if (root is None):
            return 0
        left_size = self._Size(root.left)
        right_size = self._Size(root.right)

        return left_size+right_size +1
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
        if (root.left is None):
            temp = root
            # print(root is None)
            root = None
            return temp
        return self._FindLast(root.left,index,node_count)
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
        last_node = self._FindLast(self.root, 0, self._Size(self.root))
        # print(f"the last node is {last_node is None}")
        root.data = last_node.data
        del last_node

    def _PreOrder(self,root):
        if (root is None):
            return
        print(f"{root.data},")
        self._PreOrder(root.left)
        self._PreOrder(root.right)
    def _InOrder(self,root):
        if (root is None):
            return
        self._InOrder(root.left)
        print(root.data)
        self._InOrder(root.right)
    def _PostOrder(self,root):
        if (root is None):
            return
        self._PostOrder(root.left)
        self._PostOrder(root.right)
        print(root.data)
    '''this is where all of the above functions will get called'''
    def DeleteQueue(self):
        self._Delete(self.root)
    def Insert(self,data,key = None):
        if (isinstance(data,dict)):
            self.root = self._InsertDict(data, self.root,key)
        else:
            self.root = self._Insert(data,self.root)
        self.dictionary = isinstance(data,dict)
    def Height(self):
        return self._Height(self.root)
    def PreOrder(self):
        self._PreOrder(self.root)
    def PostOrder(self):
        self._PostOrder(self.root)
    def Inorder(self):
        self._InOrder(self.root)
    def Search(self,data,key = None):
        if (self.dictionary):
            return self._SearchDict(data = data, root = self.root,key = key)
        else:
            return self._Search(data= data, root = self.root)
    def IsFull(self):
        return self._IsFull(self.root)
    def IsComplete(self):
        return self._IsComplete(self.root,0, self._Size(self.root))
    def RemoveMax(self, key = None):
        # print(self.root.data)
        if (self._Size(self.root)>1):
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
        # print(type(self.root))
        temp = self._FindLast(self.root, 0, self._Size(self.root))
        print(temp)
        return temp
    def Heapify(self, key = None):
        if (self.dictionary):
            self._MaxHeapifyDict(root = self.root, key = key)
        else:
            self._MaxHeapify(root = self.root)
    def ConvertToList(self):
        self.sorted_data = []
        for i in range(self._Size(self.root)):
            self.sorted_data.append(self.root.data)
            self.RemoveMax(key = "price")
            # except AttributeError:
            #     break
    # def ConvertToQueue(self):
    #     self.data = IslanderQueue
    #     while (True):
    #         try:
    #             # print(self.queue.root.data)
    #             self.data.Push(data=self.queue.root.data)
    #             self.RemoveMax(key="price")
    #         except AttributeError:
    #             break
            
    def Convert(self,type ="queue"):
       self.Heapify(key = "price")
       # temp = self.root
       # if (type=="queue"):
       #     self.ConvertToQueue()
       #  elif (type == "list"):
       self.ConvertToList()
        # self.root = temp
if __name__ == "__main__":
    # t=Heap()
    # t.Insert(5);
    # t.Insert(3);
    # t.Insert(7);
    # t.Insert(2);
    # t.Insert(4);
    # t.Insert(6);
    # t.Insert(1);
    # t.Insert(9);
    # t.Insert(18);
    # t.Insert(81);
    # t.PreOrder()
    data = Heap()
    data.Insert({'price': 9.73, 'symbols': 'ADRA', 'percentage': 0.12},key = "price")
    data.Insert({'price': 7.57, 'symbols': 'APT', 'percentage': 0.49},key = "price")
    data.Insert({'price': 4.0, 'symbols': 'BTG', 'percentage': 0.05},key = "price")
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key = "price")
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")
    data.Insert({'price': .22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")
    print(data._Size(data.root.left) == data._Size(data.root.right))
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
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price") #10 11 18 19
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")
    data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")#22
    # data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")#23
    # data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")
    data.Convert()
    for i in data.sorted_data:
        print(i)
    # print(data._Size(data.root))
    # print(data.PostOrder())
    # print(type(data.root))
    # print(data.root.data)
    # data.Insert({'price': 2.22, 'symbols': 'AXU', 'percentage': 0.02}, key="price")
    # data.FindLast()
    # print(data.root.data)
    # data.Insert(5);
    # data.Insert(3);
    # data.Insert(7);
    # data.Insert(2);
    # data.Insert(4);
    # data.Insert(6);
    # data.Insert(8);
    # data.PreOrder()
    # print(data.FindLast())
    # print(data.IsFull())
    # print(data.IsComplete())
    # data.Heapify(key="price")
    # data.PostOrder()
    # print(data.root.data)
    # data.RemoveMax(key="price")
    # print(data.root.data)
    # data.RemoveMax(key="price")
    # print(data.root.data)
    # data.Heapify(key="price")
    # data.PostOrder()
    # data.RemoveMax
    # data.Convert(type = "list")
    # for  i in data.sorted_data:
    #     print(i)
    # data.PostOrder()
    # print(data.Height())
    # print(data.IsComplete())
    # # print(data.Search(101, key = "price"))
    # print(data.IsFull())
    # data.RemoveMax()
    # data.RemoveMax()
    # # data.DeleteElement(8)
    # data.PostOrder()
    # # {'price': 4.0, 'symbols': 'BTG', 'percentage': 0.05}
    # # {'price': 4.1, 'symbols': 'AWX', 'percentage': 0.09}
