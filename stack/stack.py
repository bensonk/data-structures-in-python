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
