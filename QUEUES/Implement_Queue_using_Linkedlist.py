# Implement a Queue using Linked List. 
# A Query Q is of 2 Types
# (i) 1 x   (a query of this type means  pushing 'x' into the queue)
# (ii) 2     (a query of this type means to pop an element from the queue and print the poped element)

# Example 1:

# Input:
# Q = 5
# Queries = 1 2 1 3 2 1 4 2
# Output: 2 3
# Explanation: n the first testcase
# 1 2 the queue will be {2}
# 1 3 the queue will be {2 3}
# 2   poped element will be 2 the
#     queue will be {3}
# 1 4 the queue will be {3 4}
# 2   poped element will be 3.

# ============PYTHON CODE===============

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def push(self, data): 
         
         #Add code here
        item_node = Node(data)
        if self.head is None:
            self.head = item_node
            self.tail = item_node
        else:
            self.tail.next = item_node
            self.tail = item_node
    
    #Function to pop front element from the queue.
    def pop(self):
         
         #add code here
        if self.head == None:
            return -1
        item = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail=None
        return item