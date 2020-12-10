import sys
import functools

lines = [int(l.strip()) for l in open('input.txt').readlines()]

# Part 1:
def find_match(i, j, l):
  for _i in range(i, j-1):
    for _j in range(_i+1, j):
      if (lines[_i] + lines[_j]) == l:
        return (lines[_i], lines[_j])
  return False

def part_1():
  i, j = (0, 25)
  for l in lines[25:]:
    m = find_match(i, j, l)
    if not m:
      print("Couldn't find pairs that sum up to %s" % l)
      sys.exit()
    i, j = (i+1, j+1)

# part_1()

# Part 2:
def find_set(arr, n):
  print("Finding set for l: %s" % n)
  s = 0
  while s < len(arr):
    _n = n
    for i in range(s, len(arr)):
      _n -= arr[i]
      if _n == 0:
        return arr[s:i+1]
      if _n < 0:
        break
    s += 1

def part_2():
  i, j = (0, 25)
  for l in lines[25:]:
    m = find_match(i, j, l)
    if not m:
      result = find_set(lines[0:j], l)
      print(result)
      print("min: %s max: %s = %s" % (min(result), max(result), min(result) + max(result)))
      sys.exit()
    i, j = (i+1, j+1)

part_2()