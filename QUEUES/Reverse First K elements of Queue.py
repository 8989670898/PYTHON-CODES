# Given an integer K and a queue of integers, we need to reverse the order of the first K elements of the queue, leaving the other elements in the same relative order.

# Only following standard operations are allowed on queue.

# enqueue(x) : Add an item x to rear of queue
# dequeue() : Remove an item from front of queue
# size() : Returns number of elements in queue.
# front() : Finds front item.
# Note: The above operations represent the general processings. In-built functions of the respective languages can be used to solve the problem.
# Example 1:

# Input:
# 5 3
# 1 2 3 4 5

# Output: 
# 3 2 1 4 5

# Explanation: 
# After reversing the given
# input from the 3rd position the resultant
# output will be 3 2 1 4 5.



# =================PYTHON_CODE============================

from collections import deque

def reverse_Kelement(q,k):
    dq=deque()
    count=0
    for i in q:
        if count<k:
            dq.appendleft(i)
            count+=1
        else:
            dq.append(i)
    return dq

