#!/usr/bin/env python

class HashTable(object):
  def __init__(self, size=100):
    self.data = [None] * size

  def add(self, item):
    # TODO

if __name__ == "__main__":
  h = HashTable()
  print h.data
