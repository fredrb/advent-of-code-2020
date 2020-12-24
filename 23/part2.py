class Node():
  def __init__(self, value, n=None, p=None):
    self.next = n
    self.prev = p
    self.value = value

class CircularLinkedList():
  def __init__(self, initializer, part2=False):
    if part2:
      bootstrap = [i for i in range(1, 1000001)]
      for i in range(0, len(initializer)):
        bootstrap[i] = initializer[i]
      print(len(bootstrap))
      print(bootstrap[:20])
      print(bootstrap[-20:])

      self.head = Node(bootstrap[0])
      cn = self.head
      for l in bootstrap[1:]:
        cn.next = Node(l, None, cn)
        cn = cn.next
      cn.next = self.head
      self.head.prev = cn
    else:
      self.head = Node(initializer[0], None)
      cn = self.head
      for v in reversed(initializer[1:]):
        cn = Node(v, cn)
        cn.next.prev = cn
      self.head.next = cn
      cn.prev = self.head
    self.node_map = {}
    test_list = []
    cn = self.head
    while True:
      test_list.append(cn.value)
      self.node_map[cn.value] = cn
      cn = cn.next
      if cn == self.head:
        break

  def append(self, triplet, anchor, after=0):
    # c = self.find_back_from(anchor, after)
    c = self.find_in_map(after)
    if not c:
      return None
    last = c.next
    c.next = triplet[0]
    triplet[0].prev = c
    triplet[2].next = last
    last.prev = triplet[2]
    return True

  def remove_after(self, node):
    removed = []
    # root = node
    cn = node.next
    for _ in range(0, 3):
      if cn == self.head:
        self.head = node
      removed.append(cn)
      cn = cn.next
    node.next = cn
    cn.prev = node
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

  def find_in_map(self, value):
    return self.node_map[value]

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

# cl = CircularLinkedList(example)

def play(cl, rounds, log=False):
  n = None
  last_i = 0
  for i in range(1, rounds+1):
    last_i = i
    if i % 1000000 == 0:
      print("-- move %s --" % i)
    if log:
      print("-- move %s --" % i)
      print("cups: %s" % cl.get_array_from(cl.head.value, 10))
    if not n:
      n = cl.head
    else:
      n = cl.find_in_map(n.value).next
    pick = cl.remove_after(n)
    picked_value = [p.value for p in pick]
    if log:
      print("   %s" % n.value)
      print("pick up: %s" % picked_value)
    destination = n.value - 1
    if destination == 0:
        destination = max(cl.node_map.keys())
    while destination in picked_value:
      destination -= 1
      if destination == 0:
        destination = max(cl.node_map.keys())
    if log:
      print("destination: %s" % destination)
    r = cl.append(pick, n, destination)
    if not r and log:
      print("Failed to append")
    if log:
      print("")
  print("Last round played: %s" % last_i)
  return cl

def part_1(log, s):
  cl = CircularLinkedList(s)
  cl = play(cl, 100, log)
  print(''.join([str(i) for i in cl.get_array_from(1, 9)[1:]]))

def part_2(log, s):
  cl = CircularLinkedList(s, True)
  cl = play(cl, 10000000, log)
  n = cl.find_in_map(1)
  print(n.value)
  l = n.next.value
  r = n.next.next.value
  print("%s * %s = %s" % (l, r, l*r))

example = [3, 8, 9, 1, 2, 5, 4, 6, 7]
puzzle = [9, 2, 5, 1, 7, 6, 8, 3, 4]

# part_1(False, example)
part_2(False, puzzle)