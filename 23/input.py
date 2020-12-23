class Node():
  def __init__(self, value, n=None, p=None):
    self.next = n
    self.prev = p
    self.value = value

class CircularLinkedList():
  def __init__(self, initializer, part2=False):
    if part2:
      print("initializing circular list with 1M position")
      self.head = Node(0)
      cn = self.head
      for i in range(1, 1000001):
        cn.next = Node(i, None, cn)
        cn = cn.next
      cn.next = self.head
      self.head.prev = cn

      cn = self.head
      for v in initializer:
        cn.value = v
        cn = cn.next
      print("done")
    else:
      self.head = Node(initializer[0], None)
      cn = self.head
      for v in reversed(initializer[1:]):
        cn = Node(v, cn)
        cn.next.prev = cn
      self.head.next = cn
      cn.prev = self.head

  def append(self, triplet, anchor, after=0):
    c = self.find_back_from(anchor, after)
    if not c:
      return None
    cn = c.next
    for v in reversed(triplet):
      cn = Node(v, cn)
      cn.next.prev = cn
    c.next = cn
    return True

  def remove_after(self, node):
    removed = []
    root = node
    node = node.next
    for _ in range(0, 3):
      if node == self.head:
        self.head = root
      removed.append(node.value)
      node = node.next
    root.next = node
    node.prev = root
    return removed

  def get_index(self, i):
    n = self.head
    for _ in range(0, i):
      n = n.next
    return n

  def find(self, value):
    n = self.head
    while True:
      if n.value == value:
        return n
      else:
        n = n.next
      if n == self.head:
        return None

  def find_back_from(self, start, value):
    n = start.prev
    while True:
      if n.value == value:
        return n
      n = n.prev
      if n == start:
        return None

  def get_array_from(self, v, until):
    n = self.find(v)
    if n is None:
      print("FIND FAILED FOR V %s" % v)
    start = n
    v = []
    for _ in range(0, until):
      v.append(n.value)
      n = n.next
    return v

cl = CircularLinkedList(example)

def play(cl, rounds, log=False):
  n = None
  for i in range(1, rounds+1):
    if log:
      print("-- move %s --" % i)
      print("cups: %s" % cl.get_array_from(cl.head.value, 10))
    if not n:
      n = cl.head
    else:
      n = n.next
    pick = cl.remove_after(n)
    if log:
      print("   %s" % n.value)
      print("pick up: %s" % pick)
    destination = n.value - 1
    if destination == 0:
        destination = 9
    while destination in pick:
      destination -= 1
      if destination == 0:
        destination = 9
    if log:
      print("destination: %s" % destination)
    r = cl.append(pick, n, destination)
    if not r and log:
      print("Failed to append")
    if log:
      print("")
  return cl

def part_1(log, s):
  cl = CircularLinkedList(s)
  cl = play(cl, 100, log)
  print(''.join([str(i) for i in cl.get_array_from(1, 9)[1:]]))

def part2(log, s):
  cl = CircularLinkedList(s, True)
  cl = play(cl, 10000000, log)
  (l, r) = cl.get_array_from(1, 3)[1:]
  print("%s * %s = %s" % (l, r, int(l)*int(r)))

example = [3, 8, 9, 1, 2, 5, 4, 6, 7]
puzzle = [9, 2, 5, 1, 7, 6, 8, 3, 4]

part_1(True, puzzle)