#!usr/bin/env python3

"""
atds_tester.py
Runs a series of tests on the atds module, including looking at 
    * Stack
    * Queue
    * Deque
@author Richard White
@version 2017-03-13
"""

from atds import *

def main():

#################################################################

    print("Testing the Stack class")
    tests_passed = 0
    try:
        s = Stack()
        tests_passed += 1
        print("Test passed: stack created")
    except:
        print("Test failed: couldn't initialize stack")

    try:
        s.push("hello")
        s.push(3)
        tests_passed += 1
        print("Test passed: items pushed")
    except:
        print("Test failed: couldn't push onto stack")

    try:
        result = s.peek()
        if (result == 3): 
            tests_passed += 1
            print("Test passed: peeked at item")
        else: 
            print("Test failed: incorrect peek value")
    except:
        print("Test failed: couldn't peek at stack")

    try:
        result = s.pop()
        if (result == 3): 
            tests_passed += 1
            print("Test passed: item popped")
        else: 
            print("Test failed: incorrect pop result")
    except:
        print("Test failed: couldn't pop")

    try:
        result = s.is_empty()
        if (not result): 
            tests_passed += 1
            print("Test passed: is_empty returned correct result")
        else: 
            print("Test failed: stack has items, but indicated empty")
    except:
        print("Test failed: is_empty() method unavailable")

    try: 
        result = s.size()
        if (result == 1): 
            tests_passed += 1
            print("Test passed: correct size returned")
        else: 
            print("Test failed: incorrect size returned")
    except:
        print("Test failed: .size() method unavailable")

    try:
        s.pop()
    except:
        pass

    try: 
        result = s.is_empty()
        if (result): 
            tests_passed += 1
            print("Test passed: .is_empty() correctly indicating empty status")
        else: 
            print("Test failed: stack failed to indicate empty status")
    except:
        print("Test failed: is_empty() unavailable")

    print(str(tests_passed) + "/7 tests passed on the Stack class")

#################################################################

    print("Testing the Queue class")
    try:
        q = Queue()
        tests_passed += 1
        print("Test passed: queue created")
    except:
        print("Test failed: couldn't initialize queue")

    try:
        q.enqueue(5)
        q.enqueue(7)
        tests_passed += 1
        print("Test passed: items enqueued")
    except:
        print("Test failed: couldn't enqueue onto queue")

    try:
        result = q.dequeue()
        if (result == 5): 
            tests_passed += 1
            print("Test passed: dequeued correct value")
        else: 
            print("Test failed: incorrect value dequeued")
    except:
        print("Test failed: couldn't dequeue")

    try: 
        result = q.size()
        if (result == 1): 
            tests_passed += 1
            print("Test passed: correct size returned")
        else: 
            print("Test failed: incorrect size returned")
    except:
        print("Test failed: .size() method unavailable")

    try:
        result = q.is_empty()
        if (not result): 
            tests_passed += 1
            print("Test passed: is_empty correctly returned false on queue")
        else: 
            print("Test failed: queue has items, but indicated empty")
    except:
        print("Test failed: is_empty() method unavailable")

    try: 
        tmp = q.dequeue() # just emptying the queue
        result = q.is_empty()
        if (result): 
            tests_passed += 1
            print("Test passed: .is_empty() correctly indicating empty status")
        else: 
            print("Test failed: queue failed to indicate empty status")
    except:
        print("Test failed: is_empty() unavailable")

    print(str(tests_passed) + "/13 tests passed on the Stack and Queue classes")

#################################################################

    print("Testing the Deque class")
    try:
        d = Deque()
        tests_passed += 1
        print("Test passed: deque created")
    except:
        print("Test failed: couldn't initialize deque")

    try:
        d.add_front(1)
        d.add_front(0)
        tests_passed += 1
        print("Test passed: items added to front")
    except:
        print("Test failed: couldn't add to front")

    try:
        d.add_rear(2)
        d.add_rear(3)
        print("Test passed: items added to rear")
    except:
        print("Test failed: couldn't add to rear")
   
    try:
        result = d.remove_front()
        if result == 0:
            tests_passed += 1
            print("Test passed: remove_front retrieved correct value")
        else: 
            print("Test failed: incorrect value remove_fronted")
    except:
        print("Test failed: couldn't use remove_front method")

    try: 
        result = d.remove_rear()
        if (result == 3): 
            tests_passed += 1
            print("Test passed: correct value removed from rear")
        else: 
            print("Test failed: incorrect value removed from rear")
    except:
        print("Test failed: .remove_rear() method unavailable")

    try:
        result = d.is_empty()
        if (not result): 
            tests_passed += 1
            print("Test passed: is_empty correctly returned false on deque")
        else: 
            print("Test failed: deque has items, but indicated empty")
    except:
        print("Test failed: is_empty() method unavailable")

    try: 
        if d.size() == 2:
            tests_passed += 1
            print("Test passed: .size() returned correct value")
        else: 
            print("Test failed: .size() return incorrect value") 
    except:
        print("Test failed: .size() unavailable")

    try:
        tmp = d.remove_front()
        tmp = d.remove_front()
        result = d.is_empty()
        if (result): 
            tests_passed += 1
            print("Test passed: is_empty correctly returned True on deque")
        else: 
            print("Test failed: deque empty, but indicated notEmpty")
    except:
        print("Test failed: is_empty() method unavailable")

#################################################################

    print("Testing the Node class")
    try:
        n = Node("data1")
        tests_passed += 1
        print("Test passed: node created")
    except:
        print("Test failed: couldn't initialize node")

    print(str(tests_passed) + "/21 tests passed on the Stack, Queue, and Deque classes") 

if __name__ == "__main__":
    main()