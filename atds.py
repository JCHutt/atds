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
            
class BinarySearcher(object):
    """Performs a binary search on a list of ordered numbers"""
    def search(nums,target):
        lower = 0
        higher = len(nums)
        while (higher-lower) > 0:
            mid = (higher+lower) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                lower = mid+1
            else:
                higher = mid-1
        if ((higher+lower) // 2) >= len(nums):
            return None
        elif nums[(higher+lower) // 2] == target: 
            return (higher+lower) // 2
        else:
            return None
        

class BinarySearcherRecursive(object):
    """Performs a recursive binary search on an ordered list of numbers"""
    def search(nums: list,target: int,lower: int, upper: int):
        if lower > upper or upper < lower or lower > len(nums)-1 or upper < 0:
            return None
        mid = (upper + lower) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            return BinarySearcherRecursive.search(nums,target,mid+1,upper)
        else:
            return BinarySearcherRecursive.search(nums,target,lower,mid-1)


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
    
class HashTable(object):
    """Initializes the Hash Table"""

    def __init__(self, size):
        """Constructs parallel lists for our hash table"""
        self.keys = size * [None]
        self.values = size * [None]
        self.size = size
        self.entries = 0
    
    def __repr__(self):
        """Returns a string representation of the hash table"""
        return "Keys: " + str(self.keys) + "\n" + "Values: " + str(self.values)
    
    def hash_function(self, key, m):
        """Calculates a hashed index based on the modulo hash function """
        return key % m

    def put(self, key, value):
        """Inserts a key and value into its corresponding spot in the hash table, including if collisions occur"""
        hash = self.hash_function(key, self.size)
        if self.entries / self.size != 1:
            while self.keys[hash] != None and self.keys[hash] != key:
                # scoot it over 
                hash = (hash + 1) % self.size
            if self.keys[hash] == None:
                self.entries += 1
            self.keys[hash] = key
            self.values[hash] = value

    def get(self,key):
        """Finds and return the value in the hash table for a given key"""
        hash = self.hash_function(key, self.size)
        while self.keys[hash] != None and self.keys[hash] != key:
            hash = (hash + 1) % self.size
        return self.values[hash]
    
    def __len__(self):
        """Returns the number of values in the hash table"""
        return self.entries


def main():

    #Testing Binary searching 
    b = BinarySearcher()
    nums = [3,5,7,20,26,90,100]
    print(BinarySearcher.search(nums,7))
    print(BinarySearcherRecursive.search(nums,101,0,len(nums)))
    print(BinarySearcherRecursive.search(nums,1,0,len(nums)))
    print(BinarySearcherRecursive.search(nums,3,0,len(nums)))
    print(BinarySearcherRecursive.search(nums,5,0,len(nums)))
    print(BinarySearcherRecursive.search(nums,7,0,len(nums)))
    print(BinarySearcherRecursive.search(nums,20,0,len(nums)))
    print(BinarySearcherRecursive.search(nums,26,0,len(nums)))
    print(BinarySearcherRecursive.search(nums,90,0,len(nums)))
    print(BinarySearcherRecursive.search(nums,100,0,len(nums)))


    tests_passed = 0
    print("\nTEST: Creating HashTable(11)...")
    try:
        h = HashTable(11)
        tests_passed += 1
        print("SUCCESS. Table created.")
    except:
        print("FAIL. Table not created.")
    
    print("\nTEST: Using put function to store key-value pairs in table...")
    try:
        h.put(1, "a")
        h.put(6, "e")
        h.put(10, "f")
        h.put(12, "b")
        h.put(23, "c")
        tests_passed += 1
        print("SUCCESS. .put() method called with 5 values.")
    except:
        print("FAIL. Problem with .put() method.")
    
    print("\nTEST: Trying to print the current state of table...")
    try:
        print(h)
        print("Should look something like:")
        print("Keys:   [None, 1, 12, 23, None, None, 6, None, None, None, 10]")
        print("Values: [None, 'a', 'b', 'c', None, None, 'e', None, None, None, 'f']")
        tests_passed += 1
    except:
        print("FAIL. Couldn't print using __str__ or __repr__")
    
    print("\nTEST: Using put() for a function at the end of the table to see if it wraps around...")
    try:
        h.put(21, "g")
        if h.get(21) == "g":
            print("SUCCESS. .put() correctly wrapped in the table.")
            tests_passed += 1
        else:
            print("FAIL. .put() wraparound didn't work.")
        print(h)
    except:
        print("FAIL. .put() didn't correctly wrap the table in linear probe.")
    
    print("\nTEST: Checking the number of values in the hash table...")
    try:
        l = len(h)
        if l == 6:
            print("SUCCESS. len(h) is 6.")
            tests_passed += 1
        else:
            print("FAIL. len(h) should have been 5 -- solution is to write a __len__ method.")
    except:
        print("FAIL. Problem with len() method.")

    print("\nTEST: Looking for original hash in table...")
    try:
        result = h.get(10)
        tests_passed += 1
        print("SUCCESS. .get() method called.")
        if result == "f":
            tests_passed += 1
            print("SUCCESS. Correct value returned.")
        else:
            print("FAIL. Incorrect value returned.")
    except:
        print("FAIL. Problem with .get() method.")
    
    print("\nTEST: Replacing original hash {1, 'a'} in table with {1, 'z'}...")
    try:
        h.put(1, "z")
        result = h.get(1)
        if result == "z":
            print("SUCCESS. New value put and found.")
            tests_passed += 1
        else:
            print("FAIL. New value not put/found.")
    except:
        print("FAIL. Problem with replacing an old key.")
    
    print("\nTEST: Looking for key-collision in table...")
    try:
        result = h.get(23)
        tests_passed += 1
        print("SUCCESS. .get() method called.")
        if result == "c":
            tests_passed += 1
            print("SUCCESS. Correct value returned.")
        else:
            print("FAIL. Incorrect value returned.")
    except:
        print("FAIL. Problem with .get() finding a key-collision.")
    
    print("\nTEST: Looking for a hash that's not in table..")
    try:
        result = h.get(14)
        if result == None:
            tests_passed += 1
            print("SUCCESS. Non-existent value not found.")
        else:
            print("FAIL. Non-existent value found.")
    except:
        print("FAIL. Problem with .get() method.")
    
    print("\nTEST: Looking for collision not in table...")
    try:
        result = h.get(45)
        if result == None:
            tests_passed += 1
            print("SUCCESS. Non-existent collision not found.")
        else:
            print("FAIL. Non-existent collision found.")
    except:
        print("FAIL. Problem with .get() method.")
    
    print("\nResults:")
    print(tests_passed,"/ 12 tests passed")

if __name__ == "__main__":
    main()