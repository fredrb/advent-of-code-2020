puzzle = '6,13,1,15,2,0'

nums = [int(n) for n in puzzle.split(',')]
spoken = {}

t = 1
last = None

for n in nums:
  spoken[n] = (t, 0)
  last = n
  t += 1

for t in range(len(nums)+1, 2021):
  (h, l) = spoken.get(last)
  if l == 0:
    (sh, sl) = spoken.get(0)
    spoken[0] = (t, sh)
    last = 0
  else:
    s = h - l
    (sh, sl) = spoken.get(s) if spoken.get(s) is not None else (0, 0)
    spoken[s] = (t, sh)
    last = s
print("turn %s spoken %s" % (t, last))