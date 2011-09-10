#!/usr/bin/env python

class Stack(object):
  def __init__(self):
    self.data = list()

  def push(self, item):
    self.data.append(item)

  def pop(self):
    return self.data.pop()

  def peek(self):
    if self.data:
      return self.data[len(self.data)-1]
    else:
      return None

if __name__ == "__main__":
  s = Stack()

  for i in range(10):
    s.push(i)

  while(s.peek() != None):
    print s.pop()
