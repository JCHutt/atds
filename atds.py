#!/usr/bin/env python3
"""
atds.py
Advanced Topics Data Structures
A collection of data types including: Stacks, Queues, Deques
"""

__author__ = "Jujube Hutt"
__version__ = "2026-02-18"

class Stack(object):
    """Defines a stack."""
    
    def __init__(self):
        """Initializes the stack."""
        self.list = []

    def push(self, item):
        """Adds an item onto the top of the stack."""
        self.list.append(item)
    
    def peek(self):
        if len(self.list)>0:
            return self.list[-1]
    
    def pop(self):
        if len(self.list)>0:
            return self.list.pop()
    
    def size(self):
        return len(self.list)

    def is_empty(self):
        return self.size() == 0
    
    def __repr__(self):
        result = "Stack["
        while len(self.list) > 0:
            result += str(self.list[-1]) + ","
        result = result + "]"
        return result


class Queue(object):
    """Defines a queue."""
    
    def __init__(self):
        """Initializes the queue."""
        self.list = []

    def enqueue(self, item):
        """Adds an item onto the tail of the queue."""
        self.list.append(item)
    
    def peek(self):
        """Returns the item at the head of the queue, but does not remove it."""
        if len(self.list)>0:
            return self.list[0]
    
    def dequeue(self):
        """Returns and removes the item at the head of the queue."""
        if len(self.list)>0:
            return self.list.pop(0)
    
    def size(self):
        """Returns the size of the queue."""
        return len(self.list)

    def is_empty(self):
        """Returns whether or not the queue is empty."""
        return self.size() == 0
    
    def __repr__(self):
        string_rep = "Queue["
        for i in range(len(self.list)):
            string_rep += self.list[i]
            if i == len(self.list)-1:
                string_rep += "]"
            else:
                string_rep += ","
        return string_rep

class Deque(object):
    """Defines a deque."""
    
    def __init__(self):
        """Initializes the deque."""
        self.list = []

    def add_front(self, item):
        """Adds an item onto the front of the deque."""
        self.list.insert(0, item)

    def add_rear(self, item):
        """Adds an item onto the rear of the deque."""
        self.list.append(item)
    
    def remove_front(self):
        """Returns and removes the item at the front of the deque."""
        if len(self.list)>0:
            return self.list.pop(0)
        
    def remove_rear(self):
        """Returns and removes the item at the rear of the deque."""
        if len(self.list)>0:
            return self.list.pop()
    
    def size(self):
        """Returns the size of the deque."""
        return len(self.list)

    def is_empty(self):
        """Returns whether or not the deque is empty."""
        return self.size() == 0
    
    def __repr__(self):
        string_rep = "Deque["
        for i in range(len(self.list)):
            string_rep += self.list[i]
            if i == len(self.list)-1:
                string_rep += "]"
            else:
                string_rep += ","
        return string_rep

class Node(object):
    """Defines a node."""
    
    def __init__(self,data):
        """Initializes the node."""
        self.data = data
        self.next = None

    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self,new_data):
        self.data = new_data
    
    def set_next(self,new_next):
        self.next = new_next

    def __repr__(self):
        return "Node[data=" + str(self.data) + ",next=" + str(self.next) + "]"

class UnorderedList(object):
    """Defines a UnorderedList."""
    
    def __init__(self):
        """Initializes the UnorderedList."""
        self.head = None

    def add(self,item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def length(self):
        node_count = 0
        current = self.head
        while current != None:
            node_count += 1
            current = current.get_next()
        return node_count
    
    def is_empty(self):
        return self.head == None
    
    def remove(self,item):
        previous = None
        current = self.head
        while current != None:
            if current.get_data() == item:
                if previous == None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
                return
            else:
                previous = current
                current = current.get_next()
        return # default

    def search(self,item):
        if item == self.head.get_data():
            return True
        current = self.head.get_next()
        while current.get_next() != None:
            if item == current.get_data():
                return True
            else:
                current = current.get_next()
        return False
    
    def append(self,item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(new_node)

    def index(self,item):
        current = self.head
        count = 0
        while current.get_next() != None:
            if item == current.get_data():
                return count
            else:
                current = current.get_next()
                count += 1
        return count

    def insert(self,pos,item):
        new_node = Node(item)
        if pos == 0:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            count = 0
            current = self.head
            while count < pos-1:
                current = current.get_next()
                count += 1
            new_node.set_next(current.get_next())
            current.set_next(new_node)
    
    def pop(self, pos = -1):
        if self.head == None:
            return
        elif pos == -1:
            previous = None
            current = self.head
            while current.get_next() != None:
                previous = current
                current = current.get_next()
            if previous == None:
                self.head = None
            else:
                previous.set_next(None)
            return current
        elif pos == 0:
            to_remove = self.head
            self.head = self.head.get_next()
            return to_remove
        else:
            previous = None
            current = self.head
            count = 0
            while count < pos:
                previous = current
                current = current.get_next()
                count += 1
            previous.set_next(current.get_next())
            return current
    

    def __repr__(self):
        """Creates a representation of the list suitable for printing, debugging."""
        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        """
        if result[-1] == ",":
            result = result[:-1] # remove trailing comma
        """
        result = result + "]"
        return result
    
class LinearSearcher(object):  
    """Performs a linear search on a list of numbers (ordered or unordered)"""
    def search(nums,target):
        for pos in range(len(nums)):
            if nums[pos] == target:
                return pos
        return None
            

        

class BinarySearcherRecursive(object):
    """Performs a recursive binary search on an ordered list of numbers"""
    def __init__(self):
        pass

    def search(self,nums,target):
        if len(nums) == 0:
            return None
        mid = len(nums) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            self.search(self,nums[mid+1:],target)
        else:
            self.search(self,nums[:mid],target)
        return None


class ULStack(object):
    """Defines a Stack with UnorderedLists."""
    
    def __init__(self):
        """Initializes the ULStack"""
        self.list = UnorderedList()

    def push(self, item):
        self.list.insert(0,item)

    def pop(self):
        return self.list.pop(0)
    
    def peek(self):
        current = self.list.pop(0)
        self.list.insert(0,current)
        return current
    
    def size(self):
        return self.list.length()
    
    def is_empty(self):
        return self.list.is_empty()


def main():
    nums = [4,67,3,8,90]
    print(LinearSearcher.search(nums,4))
    nums2 = [3,4,5,7,20,57,300]
    print(BinarySearcher.search(nums2,20))

if __name__ == "__main__":
    main()