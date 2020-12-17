import itertools

N_COORDS = []
for c in list(itertools.combinations_with_replacement([0, -1, +1], 4)):
  N_COORDS.extend(list(set(itertools.permutations(c))))

def get_n_coords(p: (int, int, int, int)) -> [(int, int, int, int)]:
  (x, y, z, w) = p
  options = []
  for c in N_COORDS:
    if c != (0, 0, 0, 0):
      (xc, yc, zc, wc) = c
      options.append((x + xc, y + yc, z + zc, w + wc))
  return options

universe = {}
initial = [[True if c == '#' else False for c in list(l.strip())] for l in open('input.txt').readlines()]
for x in range(0, len(initial)):
  for y in range(0, len(initial)):
    if initial[y][x]:
      universe[(x,y,0,0)] = True

for _ in range(0, 6):
  next_universe = {}
  c_to_check = []
  for k in universe.keys():
    c_to_check.append(k)
    c_to_check.extend(get_n_coords(k))
  for c in c_to_check:
    active_n = [universe.get(nc) for nc in get_n_coords(c)].count(True)
    if (universe.get(c) is None and active_n == 3) or (universe.get(c) == True and active_n in range(2,4)):
      next_universe[c] = True
  universe = next_universe
print(len(universe.keys()))