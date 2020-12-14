f = [[i.strip() for i in l.split('=')] for l in open('input.txt').readlines()]

mask = ''
import itertools


def get_masked(mask, value, ignore):
  or_mask = mask.replace(ignore, '0')
  value = value | int(or_mask, 2)
  and_mask = mask.replace(ignore, '1')
  value = value & int(and_mask, 2)
  return value

def addr_masked(mask, addr):
  or_mask = int(mask.replace('X', '0'), 2)
  addr = addr | or_mask
  xs = []
  mask = mask.replace('0','Y').replace('1','Y')
  for i in range(0, len(mask)):
    if mask[i] == 'X':
      xs.append(i)
  targets = []
  for i in range(0, len(xs)+1):
    c = [list(j) for j in list(itertools.combinations(xs, i))]
    for ones in c:
      nmask = list(mask)
      for one in ones:
        nmask[one] = '1'
      nmask = ''.join(nmask).replace('X','0')
      targets.append(get_masked(nmask, addr, 'Y'))
  return sorted(targets)

mem = {}
for i in f:
  if i[0] == 'mask':
    mask = i[1]
  else:
    addr = int(i[0][4:-1])
    value = int(i[1])
    for a in addr_masked(mask, addr):
      mem[a] = value

s = 0
for i in mem.keys():
  s += mem[i]
print("Total: %s" % s)