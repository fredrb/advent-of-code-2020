seats = [list(l.strip()) for l in open('example.txt').readlines()]
width = len(seats[0])
height = len(seats)

def dline(s, c, step):
  c = (c[0] + step[0], c[1] + step[1])
  while (width > c[0] >= 0) and (height > c[1] >= 0):
    n = s[c[1]][c[0]]
    if n in ['#', 'L']:
      return n
    c = (c[0] + step[0], c[1] + step[1])
  return '.'  

def line_around(s, x, y):
  return [
    dline(s, (x, y), (-1, 0)),
    dline(s, (x, y), (+1, 0)),
    dline(s, (x, y), (0, -1)),
    dline(s, (x, y), (0, +1)),
    dline(s, (x, y), (-1, -1)),
    dline(s, (x, y), (-1, 1)),
    dline(s, (x, y), (1, 1)),
    dline(s, (x, y), (1, -1)),
  ]

found = False
i = 0
while not found:
  old = []
  for row in seats:
    old.append(row.copy())
  changed = False
  for x in range(0, len(old[0])):
    for y in range(0, len(old)):
      v = old[y][x]
      if v != '.':
        n = line_around(old, x, y)
        nv = v
        if v == 'L' and n.count('#') == 0:
          nv = '#'
        elif v == '#' and n.count('#') >= 5:
          nv = 'L'
        if nv != v:
          changed = True
          seats[y][x] = nv
  i += 1
  if changed == False:
    print("Not changed since last iteration. Current %s" % i)
    found = True

import functools 
print(functools.reduce(lambda acc,row: acc + row.count('#'), seats, 0))
