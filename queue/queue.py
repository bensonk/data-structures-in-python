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
