password = [l.strip().split(':') for l in open('input.txt').readlines()]
pol = [l[0].split(' ') for l in password]
pwd = [l[1].strip() for l in password]

match = []
for i in range(0, len(pol)):
  (r,w) = pol[i]
  (r1, r2) = [pwd[i][int(x)-1] for x in r.split('-')]
  if (r1 == w or r2 == w) and r1 != r2:
    match.append(pwd[i])

print(len(match))



