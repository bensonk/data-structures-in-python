#!/usr/bin/env python

class Queue(object):
  def __init__(self):
    self.data = list()

  def push(self, item):
    self.data.insert(0, item)

  def pop(self):
    return self.data.pop()

  def peek(self):
    if self.data:
      return self.data[-1]
    else:
      return None


if __name__ == "__main__":
  q = Queue()

  for i in range(10):
    q.push(i)

  while(q.peek() != None):
    print q.pop()
