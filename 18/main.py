from enum import Enum

expressions = [[int(n) if n.isnumeric() else n for n in list(l.strip().replace(' ', ''))] for l in open('input.txt').readlines()]

def part_1(expression, p=0) -> (int, int):
  s = 0
  op = '+'
  while p < len(expr):
    if isinstance(expr[p], int):
      if op == '+':
        s += expr[p]
      elif op == '*':
        s *= expr[p]
    elif expr[p] == '(':
      (p, inner) = part_1(expression, p+1)
      if op == '+':
        s += inner
      elif op == '*':
        s *= inner
    elif expr[p] == ')':
      return (p, s)
    else:
      op = expr[p]
    p += 1
  return (p, s)

def part_2(expr, p=0) -> (int, int):
  s = 1
  stack = []
  while p < len(expr):
    if isinstance(expr[p], int):
      if len(stack) == 0:
        stack.append(expr[p])
      else:
        if stack[len(stack)-1] == '+':
          stack.pop()
          stack.append(stack.pop() + expr[p])
        else:
          stack.append(expr[p])
    elif expr[p] == '(':
      (p, inner) = part_2(expr, p+1)
      if len(stack) == 0:
        stack.append(inner)
      else:
        if stack[len(stack)-1] == '+':
          stack.pop()
          stack.append(stack.pop() + inner)
        else:
          stack.append(inner)
    elif expr[p] == ')':
      break
    else:
      stack.append(expr[p])
    p += 1
  while len(stack) > 0:
    n = stack.pop()
    if isinstance(n, int):
      s *= n
  return (p, s)


total = 0
for expr in expressions:
  (_, s) = part_2(expr)
  total += s
print(total)
