import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if not self.value:
            return "You need a tree before you can add!"
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)  # checks value against root child's left side
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target == self.value, return it
        # go left or right based on smaller or bigger
        if self.value == target:
            return True
        if target < self.value:  # Go left
            if not self.left:  # It's not here, return False
                return False
            else:
                return self.left.contains(target)
        else:  # target must be equal to or greater than self.value so go right
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        max_value = self.value

        while self:  # keep moving right until we reach the end
            if self.value > max_value:  # if value you are iterating over is greater than max_value
                max_value = self.value  # assigning max_value to that larger value
            self = self.right  # moves to right and that becomes the new node to compare against
        return max_value  # return max value after while loop breaks due to no more nodes for comparison

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)  # apply cb function to parent/root
        if self.left:  # if current node has left
            self.left.for_each(cb)  # apply cb function to left
        if self.right:  # if current node  has right
            self.right.for_each(cb)  # apply cb function to right

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:  # If a node is passed in recursively, run code block, otherwise end
            self.in_order_print(node.left)  # pass in left
            print(node.value)  # print current value
            self.in_order_print(node.right)  # pass in right

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()  # instantiate Queue Class
        queue.enqueue(node)  # add root to (end of) queue
        while queue.len() > 0:  # While there is something in queue
            current_node = queue.dequeue()  # grab node from front of queue
        print(current_node.value)  # DO THE THING - Print current_node value
        if current_node.left:  # If left
            queue.enqueue(current_node.left)  # Add left to end of queue
        if current_node.right:  # If right
            queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()  # instantiate Stack Class
        stack.push(node)  # add root to stack
        while stack.len() > 0:  # While there is something in stack
            current_node = stack.pop()  # Grab (top) node from stack
            print(current_node.value)  # DO THE THING - Print current_node value
            if current_node.left:  # If left
                stack.push(current_node.left)  # Add left to stack
            if current_node.right:  # If right
                stack.push(current_node.right)  # Add right to stack

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
