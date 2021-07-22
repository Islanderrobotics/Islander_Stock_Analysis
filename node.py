'''this will be used for as the node class for all of the container classes'''

clas Node:
  def __init__(self,data= None,next = None):
    self.data = data
    self.next = next
    self.left = None
    self.right = None
    
