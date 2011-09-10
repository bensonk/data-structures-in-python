#!/usr/bin/env python

class HashTable(object):
  def __init__(self, size=100):
    self.data = [ list() for x in range(size) ]
    self.size = size

  def add(self, key, item):
    l = self.data[hash(key) % self.size]
    for i, tup in enumerate(l):
      if tup[0] == key:
        del l[i]
        break
    l.append((key, item))

  def get(self, key):
    for k, v in self.data[hash(key) % self.size]:
      if k == key:
        return v
    return None
