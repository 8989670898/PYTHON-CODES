# Implement a First In First Out (FIFO) queue using stacks only.

# The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the UserQueue class:

# void push(int X) : Pushes element X to the back of the queue.
# int pop() : Removes the element from the front of the queue and returns it.
# int peek() : Returns the element at the front of the queue.
# boolean empty() : Returns true if the queue is empty, false otherwise.
class UserQueue:
  def __init__(self):
      self.stack_push=[]
      self.stack_pop=[]

  def push(self, x: int) -> None:
      self.stack_push.append(x)

  def pop(self) -> int:
      """
      Removes the element from in front of queue and returns that element.
      """
      self.peek()
      return self.stack_pop.pop()

  def peek(self) -> int:
      """
      Get the front element.
      """
      if not self.stack_pop:
              while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
      return self.stack_pop[-1]
      

  def empty(self) -> bool:
      """
      Returns whether the queue is empty.
      """
      return len(self.stack_push) == 0 and len(self.stack_pop) == 0
  

  # ===============optimized way===========
class Userqueu:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)
        

    def pop(self) -> int:
        self.peek()
        return self.s2.pop()
        

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]
        

    def empty(self) -> bool:
        return not self.s1 and not self.s2