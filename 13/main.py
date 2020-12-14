# import sys

# f = open('input.txt')
# t = int(f.readline().strip())
# buses = [int(b.strip()) for b in list(filter(lambda x: x != 'x', f.readline().split(',')))]

# initial = t
# while True:
#   table = [(b, t % b) for b in buses]
#   print(table)
#   matches = list(filter(lambda b: b[1] == 0, table))
#   if len(matches) > 0:
#     print(t)
#     print(matches)
#     print(matches[0][0] * (t - initial))
#     sys.exit()
#   t += 1

import sys

f = open('example.txt')
_ = int(f.readline().strip())
buses = [b.strip() for b in f.readline().split(',')]
for b in range(0, len(buses)):
  buses[b] = (buses[b], b)
buses = [(int(b[0].strip()), b[1]) for b in list(filter(lambda b: b[0] != 'x', buses))]

print(buses)

cycle = buses[0][0]
t = cycle

while True:
  matcher = [(b[1]+t) % b[0] == 0 for b in buses]
  if all(matcher):
    print("Found: %s" % t)
    sys.exit()
  t += cycle
