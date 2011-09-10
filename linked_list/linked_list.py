#!/usr/bin/env python

class LinkedList(object):
  def __init__(self, iter_items=None):
    self.head = None
    self.last = None
    if iter_items:
      for item in iter_items:
        self.add(item)


  def remove(self, item):
    if not self.head: return False

    if self.head.payload == item:
      self.head = self.head.next
      return True
    else:
      n = self.head
      while n:
        p, n = n, n.next
        if n and n.payload == item:
          p.next = n.next
          return True
    return False


  def add(self, item):
    n = ListNode(item)
    n.next = None
    if self.last:
      self.last.next = n
      self.last = n
    else:
      self.head = self.last = ListNode(item)


  def __len__(self):
    if self.head:
      return len(self.head)
    else:
      return 0

  def __iter__(self):
    def iterator(n):
      while n:
        yield n.payload
        n = n.next
    return iterator(self.head)

  def __repr__(self):
    stuff = ", ".join((str(x) for x in self))
    return '[ %s ]' % stuff



class ListNode(object):
  def __init__(self, payload):
    self.payload = payload
    self.next = None
  
  
  def __len__(self):
    if self.next:
      return 1 + len(self.next)
    else:
      return 1



if __name__ == "__main__":
  print "Testing the linked list"
  stuff = [ 'foo', 'bar', 'quux', 'baz', 'bat' ]
  my_list = LinkedList()
  for item in stuff:
    my_list.add(item)
  my_list.remove('quux')

  for item in my_list:
    print item

  second_list = LinkedList(range(15))
  second_list.remove(0)
  second_list.remove(45)
  second_list.remove(7)
  second_list.remove(13)
  print len(second_list)
  print second_list
