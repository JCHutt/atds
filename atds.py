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

def main():
    pass

if __name__ == "__main__":
    main()