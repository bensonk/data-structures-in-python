import nose
from queue import Queue

def test_basics():
  q = Queue()

  for i in range(10):
    q.push(i)

  items = list(reversed(range(10)))
  while(q.peek() != None):
    assert q.pop() == items.pop()
