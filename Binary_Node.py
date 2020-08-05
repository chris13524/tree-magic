'''
' Class for nodes which will construct a binary tree.
'''
class BinaryNode:
  __slots__ = '_element', '_parent', '_left', '_right'            # streamline memory

  '''
  ' Constructor. Creates a node with an element, a previous node, and a next
  '   node. No paramteres are required but all can be specified.
  '''
  def __init__(self, element = None, parent_node = None, left_node = None, right_node = None):
    self._element = element                           # user's element
    self._parent = parent_node                        # parent node reference
    self._left = left_node                            # left node reference
    self._right = right_node                          # right node reference

  #------------------------------- accessors -------------------------------
  '''
  ' Returns the data element contained within this node
  '''
  def get_element(self):
    return self._element

  '''
  ' Returns a reference to the parent node
  '''
  def get_parent(self):
    return self._parent

  '''
  ' Returns a reference to the left node
  '''
  def get_left(self):
    return self._left

  '''
  ' Returns a reference to the right node
  '''
  def get_right(self):
    return self._right

  #------------------------------- mutators -------------------------------
  '''
  ' Sets the data element contained within this code and returns the
  '   data element that was previously stored there
  '''
  def set_element(self, new_element):
    element = self._element
    self._element = new_element
    return element

  '''
  ' Sets the parent node and returns the old "parent node" that this
  '   node used to point to
  '''
  def set_previous(self, new_parent):
    old_parent = self._parent
    self._parent = new_parent
    return old_parent

  '''
  ' Sets the left node and returns the old "left node" that this
  '   node used to point to
  '''
  def set_left(self, new_left):
    old_left = self._left
    self._left = new_left
    return old_left

  '''
  ' Sets the right node and returns the old "right node" that this
  '   node used to point to
  '''
  def set_right(self, new_right):
    old_right = self._right
    self._right = new_right
    return old_right
