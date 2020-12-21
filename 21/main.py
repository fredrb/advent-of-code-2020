allergen = {}

puzzle = [[s.strip().split(' ') for s in l.replace(',','').replace(')','').split('(contains')] for l in open('input.txt').readlines()]

ingridients = []
for i in [p[0] for p in puzzle]:
  ingridients.extend(i)
ingridients = list(set(ingridients))

print(ingridients)

for p in puzzle:
  for a in p[1]:
    if not allergen.get(a):
      allergen[a] = list(set(p[0]))
    else:
      allergen[a].extend(p[0])

for p in puzzle:
  for labeled in p[1]:
    allergen[labeled] = list(set(filter(lambda i: i in p[0], allergen[labeled])))
    
allergen_ing = []
for v in allergen.values():
  allergen_ing.extend(v)
allergen_ing = list(set(allergen_ing))

print(allergen_ing)

non_allergen = list(filter(lambda i: allergen_ing.count(i) == 0, ingridients))

times = 0
for p in puzzle:
  for non in non_allergen:
    times += 1 if non in p[0] else 0

print(allergen)

full_match = []
while not all([isinstance(l, str) for l in allergen.values()]):
  for k in allergen:
    if isinstance(allergen[k], list):
      rem = list(filter(lambda x: x not in full_match, allergen[k]))
      if len(rem) == 1:
        full_match.append(rem[0])
        allergen[k] = rem[0]
      else:
        allergen[k] = rem
    else:
      full_match.append(allergen[k])
  print(full_match)
  full_match = list(set(full_match))

cannonical = []
for k in sorted(allergen.keys()):
  print("%s: %s" % (k, allergen[k]))
  cannonical.append(allergen[k])
print(','.join(cannonical))