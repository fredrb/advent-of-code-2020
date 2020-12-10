
# Part 1:
# l = dict.fromkeys([int(l.strip()) for l in open('input.txt').readlines()])

# for k in l.keys():
#   l[k] = 0

# c1 = 0
# c2 = 0
# c3 = 1

# jolt = 0

# # len(list(filter(lambda x: x == 0, l.values())))
# while True:
#   if l.get(jolt+1) == 0:
#     c1 += 1
#     jolt += 1
#   elif l.get(jolt+3) == 0:
#     c3 += 1
#     jolt += 3
#   else:
#     print("No more jolts available for %s" % jolt)
#     break

# print("%s * %s = %s" % (c1, c3, (c1*c3)))

# Part 2: 
import functools

values = sorted([0] + [int(l.strip()) for l in open('input.txt').readlines()])
d = dict.fromkeys(values, 0)

def index(k):
  return k if d.get(k) is not None else None

def paths(n):
  return (list(filter(lambda x: x is not None, list((index(n+1), index(n+2), index(n+3)))))) or [max(values)+3]

def count_choice(n, d):
  if d.get(n) is None: 
    return 1
  if isinstance(d[n], list): 
    d[n] = functools.reduce(lambda acc,x: acc + count_choice(x, d), d[n], 0)
  return d[n]

for k in list(d.keys()):
  d[k] = paths(k)
print(count_choice(0, d))


