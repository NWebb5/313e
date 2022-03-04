class Queue(object):
  '''Queue implements the FIFO principle.'''
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    if(not self.isEmpty()):
      return self.queue.pop(0)
    else:
      return None
    
  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)
  
  # a string representation of this stack.
  def __str__(self):
    return str(self.queue)


class Stack(object):
    def __init__ (self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push (self, item):
        while not self.queue1.isEmpty():
            self.queue2.enqueue(self.queue1.dequeue())
        self.queue1.enqueue(item)
        while not self.queue2.isEmpty():
            self.queue1.enqueue(self.queue2.dequeue())
    
    def pop (self):
        return self.queue1.dequeue()

     # check what item is on top of the stack without removing it
    def peek(self):
        return self.queue1[len(self.queue1) - 1]

    # check if a stack is empty
    def isEmpty (self):
        return (len(self.queue1) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.queue1))

    # a string representation of this stack. 
    def __str__(self):
        return str(self.queue1)
