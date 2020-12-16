import functools
import itertools

sections = open('input.txt').read().split('\n\n')

def make_range(expr):
  (l, h) = [int(n) for n in expr.split('-')]
  return range(l, h+1)

rules_raw = []
for r in [[i.strip() for i in r.split(':')] for r in sections[0].split('\n')]:
  (name, ranges) = r
  ranges = ranges.replace('or', '').replace('  ', ' ').split(' ')
  rules_raw.append([name, ranges[0], ranges[1]])

rules = []
ranges = []
for r in rules_raw:
  range_1 = make_range(r[1])
  range_2 = make_range(r[2])
  rules.append([r[0], range_1, range_2])
  ranges.append(range_1)
  ranges.append(range_2)

tickets = [[int(n) for n in s.split(',')] for s in sections[2].split('\n')[1:]]

not_in_range = []
for t in tickets:
  lookup = t
  for r in ranges:
    lookup = list(filter(lambda x: x not in r, lookup))
  not_in_range.extend(lookup)

print(functools.reduce(lambda acc,x: acc + x, not_in_range, 0))