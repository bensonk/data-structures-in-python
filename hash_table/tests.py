import nose
from hash_table import HashTable

def test_insertion():
  h = HashTable()
  h.add(48, 'teststring')
  assert h.get(48) == 'teststring'


def test_replacement():
  h = HashTable()
  h.add(12, "foo")
  h.add(12, "bar")
  assert h.get(12) == "bar"

def test_collisions():
  h = HashTable()
  h.add(25, "foo")
  h.add(125, "bar")
  assert len(h.data[25]) == 2
  assert h.get(25) == "foo"
  assert h.get(125) == "bar"
