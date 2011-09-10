import nose
from stack import Stack

def test_basics():
  s = Stack()

  for i in range(10):
    s.push(i)

  items = range(10)
  while(s.peek() != None):
    assert items.pop() == s.pop()
