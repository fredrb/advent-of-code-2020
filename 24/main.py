raw_directions = [list(d.strip()) for d in open('input.txt').readlines()]

puzzle = []
for d in raw_directions:
  i = 0
  directions = []
  while i < len(d):
    if d[i] in ['e', 'w']:
      directions.append(d[i])
      i += 1
    else:
      directions.append(d[i]+d[i+1])
      i += 2
  puzzle.append(directions)

def sum_coordinates(c1, c2):
  return (c1[0] + c2[0], c1[1] + c2[1], c1[2] + c2[2])

DELTA = {
  'nw': (0, 1, -1),
  'w': (-1, 1, 0),
  'sw': (-1, 0, 1),
  'se': (0, -1, 1),
  'e': (1, -1, 0),
  'ne': (1, 0, -1)
}

grid = set()
for directions in puzzle:
  start = (0, 0, 0)
  for d in directions:
    start = sum_coordinates(start, DELTA[d])
  # hashed = hash_triplet(start)
  if start in grid:
    grid.remove(start)
  else:
    grid.add(start)

print("part 1: %s" % len(grid))

# def get_color(c, s):
#   if c in s
#   v = grid.get(hash_triplet(c))
#   if v is None:
#     return 'WHITE'
#   return 'BLACK' if v else 'WHITE'

def get_adjecent(t):
  adj = []
  for d in DELTA.values():
    adj.append(sum_coordinates(t, d))
  return adj

for i in range(0, 100):
  next_grid = set()
  to_check = set()
  for t in grid:
    to_check.add(t)
    for a in get_adjecent(t):
      to_check.add(a)

  for t in to_check:
    black = 0
    for a in get_adjecent(t):
      if a in grid:
        black += 1
    if t in grid and (black == 1 or black == 2):
      next_grid.add(t)
    elif t not in grid and black == 2:
      next_grid.add(t)
  grid = next_grid
print(len(grid))