f = [[i.strip() for i in l.split('=')] for l in open('input.txt').readlines()]

mask = ''

def get_masked(mask, value):
  # Set 1s => OR with 1s
  or_mask = mask.replace('X', '0')
  value = value | int(or_mask, 2)
  # Set 0s => AND with 0s
  and_mask = mask.replace('X', '1')
  value = value & int(and_mask, 2)
  return value

# mem = [0 for _ in range(0,9999999999)]
mem = {}
for i in range(0, len(f)):
  if f[i][0] == 'mask':
    mask = f[i][1]
  else:
    addr = int(f[i][0][4:-1])
    value = int(f[i][1])
    mem[addr] = get_masked(mask, value)
  i += 1

s = 0
for i in mem.keys():
  s += mem[i]
print("Total: %s" % s)