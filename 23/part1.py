example = [3, 8, 9, 1, 2, 5, 4, 6, 7]
puzzle = [9, 2, 5, 1, 7, 6, 8, 3, 4]

class Node():
  def __init__(self, value, n=None):
    self.next = n
    self.value = value

class CircularLinkedList():
  def __init__(self, initializer):
    self.head = Node(initializer[0], None)
    cn = self.head
    for v in reversed(initializer[1:]):
      cn = Node(v, cn)
    self.head.next = cn

  def append(self, triplet, after=0):
    c = self.find(after)
    if not c:
      return None
    cn = c.next
    for v in reversed(triplet):
      cn = Node(v, cn)
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

  def next_from(self, i):
    return self.find(i).next

  def get_array_from(self, v):
    n = self.find(v)
    if n is None:
      print("FIND FAILED FOR V %s" % v)
    start = n
    v = []
    while True:
      v.append(n.value)
      n = n.next
      if n.value == start.value:
        return v

cl = CircularLinkedList(puzzle)

n = None
for i in range(1, 101):
  print("-- move %s --" % i)
  print("cups: %s" % cl.get_array_from(cl.head.value))
  if not n:
    n = cl.head
  else:
    n = n.next
  print("   %s" % n.value)
  pick = cl.remove_after(n)
  print("pick up: %s" % pick)
  destination = n.value - 1
  if destination == 0:
      destination = 9
  while destination in pick:
    destination -= 1
    if destination == 0:
      destination = 9
  print("destination: %s" % destination)
  r = cl.append(pick, destination)
  if not r:
    print("Failed to append")
  print("")

print(''.join([str(i) for i in cl.get_array_from(1)[1:]]))
# print("cups: %s" % )

# def gc(cups, i):
#   return cups[i % len(cups)]

# def round(cups, p):
#   n = gc(cups, p)
#   picked = [gc(cups, p+1), gc(cups, p+2), gc(cups, p+3)]
#   list(filter(lambda c: c not in picked, cups))
