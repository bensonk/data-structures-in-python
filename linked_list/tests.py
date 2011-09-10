from linked_list import LinkedList

def test_basics():
  stuff = [ 'foo', 'bar', 'quux', 'baz', 'bat' ]
  my_list = LinkedList()
  for item in stuff:
    my_list.add(item)
  for a,b in zip(stuff, my_list):
    assert a == b

  my_list.remove('quux')
  stuff.remove('quux')
  
  for a,b in zip(stuff, my_list):
    assert a == b

def test_more_stuff():
  second_list = LinkedList(range(15))
  second_list.remove(0)
  second_list.remove(45)
  second_list.remove(7)
  second_list.remove(13)
  assert len(second_list) == 12
  print second_list
  for a, b in zip(second_list, [ 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 14 ]):
    assert a == b
