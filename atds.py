#!/usr/bin/env python3
"""
atds.py
Advanced Topics Data Structures
A collection of data types including: Stacks, Queues, Deques, Nodes, Trees, Heaps, Graphs, etc.
"""

__author__ = "Jujube Hutt"
__version__ = "2026-05-04"

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
    def __init__(self):
        pass

    def search(self,nums,target):
        for pos in range(len(nums)):
            if nums[pos] == target:
                return pos
        return None
            
class BinarySearcher(object):
    """Performs a binary search on a list of ordered numbers"""
    def __init__(self):
        pass
    
    def search(self,nums,target):
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
    def __init__(self):
        pass
    
    def search(self, nums: list,target: int,lower: int, upper: int):
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

class BinaryTree(object):
    def __init__(self, value = None, left = None, right = None):
        """Constructs the BinaryTree with value, left_child, and right_child"""
        self.value = value
        self.left_child = left
        self.right_child = right

    def get_root_val(self):
        return self.value
    
    def set_root_val(self,new_val):
        self.value = new_val
    
    def insert_left(self,new_left):
        left_tree = BinaryTree(new_left,self.left_child,None)
        self.left_child = left_tree

    def insert_right(self,new_right):
        right_tree = BinaryTree(new_right,None,self.right_child)
        self.right_child = right_tree
    
    def get_right_child(self):
        return self.right_child
    
    def get_left_child(self):
        return self.left_child

    def __repr__(self):
        return "BinaryTree[key=" + str(self.value) + ",left_child=" + str(self.left_child) + ",right_child=" + str(self.right_child) + "]"
    
class BinaryHeap():
    """The BinaryHeap class implements the Binary Heap Abstract 
    Data Type as a list of values, where the index p of a parent
    can be calculated from the index c of a child as c // 2.
    """
    def __init__(self):
        self.heap_list = [0]  # not used. Here just to make parent-
                             # child calculations work nicely.
        # Note that current size of heap = len(self.heapList) - 1

    def insert(self,value):
        """Inserts a value into the heap by:
        a. adding it to the end of the list, and then
        b. "percolating" it up to an appropriate position
        """
        self.heap_list.append(value)
        self.percolate_up(len(self.heap_list)-1)

    def percolate_up(self, i):
        """Beginning at i, check to see if parent above is greater than
        value at i. If so, percolate i upwards to parent's position.
        """
        if i % 2 == 0:
            while i > 1 and self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i], self.heap_list[i//2] = self.heap_list[i//2], self.heap_list[i]
                self.percolate_up(i // 2)
        else:
            while i > 1 and self.heap_list[i] < self.heap_list[(i-1)//2]:
                self.heap_list[i], self.heap_list[(i-1)//2] = self.heap_list[(i-1)//2], self.heap_list[i]
                self.percolate_up((i-1)//2)

            

    def del_min(self):
        """Removes the minimum value and returns it, along with reordering the heap so it is still valid.
        """
        thing = self.heap_list[1]
        self.heap_list[1], self.heap_list[-1] = self.heap_list[-1], self.heap_list[1]
        self.heap_list.remove(thing)
        self.percolate_down(1)
        return thing

    def percolate_down(self,i):
        """Moves the item at i down to a correct level in the heap. To
        work correctly, needs to identify the minimum child for parent i.
        """
        while 2*i + 1 < len(self.heap_list) and (self.heap_list[i] > self.heap_list[2*i] or self.heap_list[i] > self.heap_list[2*i+1]):
            if self.heap_list[2*i] < self.heap_list[2*i+1]:
                self.heap_list[i], self.heap_list[2*i] = self.heap_list[2*i], self.heap_list[i]
                self.percolate_down(2*i)
            else:
                self.heap_list[i], self.heap_list[2*i+1] = self.heap_list[2*i+1], self.heap_list[i]
                self.percolate_down(2*i+1)
        if 2*i < len(self.heap_list) and self.heap_list[i] > self.heap_list[2*i]:
            self.heap_list[i], self.heap_list[2*i] = self.heap_list[2*i], self.heap_list[i]
            



    def find_min(self):
        """Returns the minimum item in the heap, without removing it.
        """
        if len(self.heap_list) == 1:
            return None
        else:
            return self.heap_list[1]


    def is_empty(self):
        return len(self.heap_list) - 1 == 0

    def size(self):
        return len(self.heap_list) - 1

    def build_heap(self, list_of_keys):
        """Returns a new heap based on a pre-existing list of key 
        values."""
        for key in list_of_keys:
            self.insert(key)

    def __repr__(self):
        return "BinaryHeap" + str(self.heap_list)

class Vertex(object):
    """Describes a vertex object in terms of a "key" and a
    dictionary that indicates edges to neighboring vertices with
    a specified weight.
    """
    def __init__(self, key):
        """Constructs a vertex with a key value and an empty dictionary 
        in which we'll store other vertices to which this vertex is connected.
        """
        self.key = key
        self.neighbors = {}   # empty dictionary for neighboring vertices

    def set_neighbor(self, other, weight=0):
        """Adds a reference to a neighboring Vertex object to the dictionary, 
        to which this vertex is connected by an edge. If a weight is not indicated, 
        default weight is 0.
        """
        self.neighbors[other] = weight

    def __repr__(self):
        """Returns a representation of the vertex and its neighbors, suitable for 
        printing. Check out the example of 'list comprehension' here!
        """
        return f"Vertex({self.key}"
        
    def __str__(self):
        return ( f"{self.key} connected to: " 
        + f"{[x.key for x in self.neighbors]}")

    def get_neighbors(self):
        return self.neighbors.keys()

    def get_key(self):
        return self.key

    def get_neighbor(self, other):
        """Returns the weight of an edge connecting this vertex with another,
        or None if the neighbor doesn't exist
        """
        return self.neighbors.get(other, None)
    

class Graph(object):
    """Describes the Graph class, which is primarily a dictionary
    mapping vertex names to Vertex objects, along with a few methods
    that can be used to manipulate them.
    """
    def __init__(self):
        self.vertices = {}

    def set_vertex(self, key):
        self.vertices[key] = Vertex(key)

    def get_vertex(self, key):
        """Looks for the key in the dictionary of Vertex objects, and
        returns the Vertex if found. Otherwise, returns None.
        """
        '''
        # This is the classic way of doing that
        if key in self.graph.keys():
            return self.graph[key]
        else:
            return None
        '''
        # Single-line alternative
        return self.vertices.get(key, None)

    def __contains__(self, key):
        """This 'dunder' expression is written so we can use Python's "in"
        operation: If the parameter 'key' is in the dictionary of vertices,
        the value of "key in my_graph" will be True, otherwise False.
        """
        return key in self.vertices

    def add_edge(self, from_vert, to_vert, weight=0):
        """Adds an edge connecting two vertices (specified by key
        parameters) by modifying those vertex objects. Note that
        the weight can be specified as well, but if one isn't
        specified, the value of weight will be the default value
        of 0.
        """
        # if the from_key doesn't yet have a vertex, create it
        if from_vert not in self.vertices:
            self.set_vertex(from_vert)
        # if the to_key doesn't yet have a vertex, create it
        if to_vert not in self.vertices:
            self.set_vertex(to_vert)
        # now we can create the edge between the two
        self.vertices[from_vert].set_neighbor(self.vertices[to_vert], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        """Another 'dunder' expression that allows us to iterate through
        the list of vertices.
        Example use:
        for vertex in graph:  # Python understands this now!
            print(vertex)
        """
        return iter(self.vertices.values())

def main():

    g = Graph()
    g.add_edge("V0", "V1", 2)
    g.add_edge("V1","V2",1)
    g.add_edge("V1","V3",5)
    g.add_edge("V3","V2",7)
    g.add_edge("V2","V4",2)
    g.add_edge("V4","V3",4)
    g.add_edge("V5","V4",6)
    g.add_edge("V0","V5",12)
    for vertex in g:
        print(vertex)
        for n in vertex.get_neighbors():
            print("\t", n.get_key(), n.neighbors)

if __name__ == "__main__":
    main()