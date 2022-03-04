class Stack (object):

  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append(item)

  # remove an item from the top of the stack
  def pop(self):
    if(not self.isEmpty()):
      return self.stack.pop()
    else:
      return None

  # check what item is on top of the stack without removing it
  def peek(self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size(self):
    return (len(self.stack))

  # a string representation of this stack. 
  def __str__(self):
    return str(self.stack)


class Queue (object):
    def __init__ (self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, element):
        # O(1) complexity because the argument is called 1 time
        self.stack1.push(element)

    def dequeue (self):
        # O(n) time complexity, because you use the while loop to push and pop between the stacks, n times.
        if not self.stack2.isEmpty():
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def isEmpty (self):
        return (len (self.stack1) == 0)

    def size (self):
        return len (self.stack1)
    
    # a string representation of this stack.
    def __str__(self):
        return str(self.stack1)

        

        

