'''this will be the parrent class for all tree data structors'''

from node import Node
class Tree:
  def __init__(self):
    self.root = None

  def _Size(self, root):
    if (root is None):
      return 0
    left_size = self._Size(root.left)
    right_size = self._Size(root.right)

    return left_size + right_size + 1

  def _Height(self, root):
    if (root is None):
      return -1
    left = self._Height(root.left)
    right = self._Height(root.right)
    if (left > right):
      return (left + 1)
    else:
      return (right + 1)

  def _PreOrder(self,root):
    if (root is None):
      return
    print(root.data)
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

  def _IsFull(self, root):
    if root is None:
      return False
    if (root.left is None and root.right is None):
      return True
    if (root.left is not None and root.right is not None):
      return self._IsFull(root.left) and self._IsFull(root.right)
    return False

  def _IsComplete(self, root, index, node_count):
    if root is None:
      return True
    if (index >= node_count):
      return False

    left_completed = self._IsComplete(root.left, 2 * index + 1, node_count)
    right_completed = self._IsComplete(root.right, 2 * index + 2, node_count)
    return left_completed and right_completed

  def Height(self):
    return self._Height(self.root)
  def PreOrder(self):
    self._PreOrder(self.root)
  def PostOrder(self):
    self._PostOrder(self.root)
  def Inorder(self):
    self._InOrder(self.root)
  def Size(self):
    return self._Size(self.root)
  def IsFull(self):
      return self._IsFull(self.root)
  def IsComplete(self):
      return self._IsComplete(self.root,0, self._Size(self.root))