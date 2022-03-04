class Link(object):
  ''' This class represents a link between data items only'''
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

  def __str__(self):
    return str(self.data) + " --> " + str(self.next)

class LinkedList(object):
  ''' This class implements the operations of a simple linked list'''
  def __init__ (self):
    self.first = None

  def insertFirst (self, data):
    '''inset data at begining of a linked list'''
    newLink = Link(data)
    newLink.next = self.first
    self.first = newLink

  def insertLast (self, data):
    ''' Inset the data at the end of a linked list '''
    newLink = Link(data)
    current = self.first

    if (current == None):
      self.first = newLink
      return
    # find the last and insert it there. 
    while (current.next != None):
      current = current.next

    current.next = newLink

  def findLink(self, data):
    ''' find to which data is the link of a given data inside this linked list'''
    current = self.first
    if (current == None):
      return None

    # searcg and find the position of the given data, the get the link if. 
    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next

    return current

  def deleteLink(self, data):
    ''' Removes the data from the list if exist and fix the link problems.'''

    current = self.first
    previous = self.first

    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        previous = current
    
      current = current.next

    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next

    return current

  def __str__(self):
      return str(self.first)

class Stack (object):
    def __init__(self):
        self.linked_head = LinkedList()

    def push(self, item):
        if self.linked_head == None:
            self.linked_head = Link(item)
        else:
            self.linked_head.insertFirst()

    def pop(self):
        if self.linked_head == None:
            return None
        else:
            return self.linked_head.deleteLink()
    
    def peek(self):
        if self.linked_head == None:
            return None
        else:
            return self.linked_head.data

    def isEmpty (self):
        if self.linked_head == None:
            return True
        else:
            return False
    
    def __str__(self):
        return str(self.linked_head)
    


    