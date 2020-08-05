# Christopher Smith
# 46062
# CISC 160-01
# Lab 04

# Import statements go here
from Binary_Node import BinaryNode
import math
import random
import time

'''
Function which takes the root node of a sorted binary tree and an element.
  This function finds where in the binary tree that the element should be
  inserted (by using the algorithm provided in the lab booklet) so that the
  the tree stays in order.
PARAM:   root_node      The root of the linked list
PARAM:   new_element    The new element to be added into the list
RETURNS: The node at the root of the sorted binary tree.
'''
def insert(root_node, new_element):
    if root_node == None:
        return BinaryNode(new_element)
    current_node = root_node
    while True:
        if new_element < current_node.get_element():
            if current_node.get_left() == None:
                current_node.set_left(BinaryNode(new_element, current_node))
                return root_node
            current_node = current_node.get_left()
        else:
            if current_node.get_right() == None:
                current_node.set_right(BinaryNode(new_element, current_node))
                return root_node
            current_node = current_node.get_right()

'''
Function which takes the root node of a sorted binary tree and an element.
  This function searchs the tree for that element using an iterative
  methodology. As it goes, the function creates a path of element in the nodes
  traversed and returns that path at the end.
PARAM:   root_node      The root of the linked list
PARAM:   element        The element to be found in the tree
RETURNS: The path through the tree from the root to the element's node, or
           None if the element cannot be found in the tree.
'''
def iterative_path(root_node, element):
    path = []
    while root_node != None:
        path.append(root_node.get_element())
        if element == root_node.get_element():
            return path
        elif element < root_node.get_element():
            root_node = root_node.get_left()
        else:
            root_node = root_node.get_right()
    return None

'''
Function which takes the root node of a sorted binary tree and an element.
  This function searchs the tree for that element using a recursive
  methodology. As it goes, the function creates a path of element in the nodes
  traversed and returns that path at the end.
PARAM:   root_node      The root of the linked list
PARAM:   element        The element to be found in the tree
RETURNS: The path through the tree from the root to the element's node, or
           None if the element cannot be found in the tree.
'''
def recursive_path(root_node, element):
    if root_node == None: return None
    if element == root_node.get_element():
        return [root_node.get_element()]
    elif element < root_node.get_element():
        return [root_node.get_element()] + recursive_path(root_node.get_left(), element) or []
    else:
        return [root_node.get_element()] + recursive_path(root_node.get_right(), element) or []

def to_tree(array):
    root_node = None
    for e in array:
        root_node = insert(root_node, e)
    return root_node

def from_tree(root_node):
    if root_node == None: return None
    if root_node.get_left() == None and root_node.get_right() == None: return (root_node.get_element())
    return (root_node.get_element(), from_tree(root_node.get_left()), from_tree(root_node.get_right()))

SPACE = " "
NULL = u"\u2591"
LINE = u"\u2500"
LEFT_ANGLE = u"\u250C"
RIGHT_ANGLE = u"\u2510"
def render_tree(root_node):
    if root_node == None: return NULL
    left_lines = render_tree(root_node.get_left()).split("\n")
    right_lines = render_tree(root_node.get_right()).split("\n")
    left_width = len(left_lines[0])
    element = str(root_node.get_element())
    for i in range(left_width):
        if left_lines[0][i] != SPACE and left_lines[0][i] != LEFT_ANGLE and left_lines[0][i] != LINE:
            left_root_index = i
            break
    right_width = len(right_lines[0])
    for i in range(right_width):
        if right_lines[0][i] != SPACE and right_lines[0][i] != LEFT_ANGLE and right_lines[0][i] != LINE:
            right_root_index = i
            break
    render = SPACE * (left_root_index)
    render += LEFT_ANGLE
    render += LINE * (left_width-left_root_index-1)
    render += element
    render += LINE * right_root_index
    render += RIGHT_ANGLE
    render += SPACE * (right_width-right_root_index-1)
    render += "\n"
    for i in range(max(len(left_lines), len(right_lines))):
        if i >= len(left_lines):
            render += SPACE * left_width
        else:
            render += left_lines[i]
        render += SPACE * len(element)
        if i >= len(right_lines):
            render += SPACE * right_width
        else:
            render += right_lines[i]
        render += "\n"
    return render[:-1]

def testInsert(array):
    return from_tree(to_tree(array))

def testPath(array, element, path):
    assert iterative_path(to_tree(array), element) == path
    assert recursive_path(to_tree(array), element) == path

# Test code can go below if you want
if __name__ == '__main__':
    assert testInsert([]) == None
    assert testInsert([1]) == (1)
    assert testInsert([1, 2]) == (1, None, (2))
    assert testInsert([1, 2, 0]) == (1, (0), (2))
    assert testInsert([3, 2, 1]) == (3, (2, (1), None), None)

    testPath([], 1, None)
    testPath([1], 1, [1])
    testPath([1, 2], 1, [1])
    testPath([1, 2], 2, [1, 2])
    testPath([1, 2, 3], 3, [1, 2, 3])
    testPath([3, 2, 1], 3, [3])
    testPath([3, 2, 1], 1, [3, 2, 1])
    testPath([2, 1, 3], 2, [2])
    testPath([2, 1, 3], 1, [2, 1])

    elements = []
    for x in range(50): elements.append(random.randint(111, 999))
    print(render_tree(to_tree(elements)))
