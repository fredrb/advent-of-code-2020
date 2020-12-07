# import functools
# g = open('./input.txt').read().split('\n\n')
# print(functools.reduce(lambda acc, x: acc + len(x), [list(dict.fromkeys([char for char in i.replace('\n','')])) for i in g], 0))

import functools
count = 0
for g in open('./input.txt').read().split('\n\n'):
    members = [m for m in g.split('\n')]
    group_ans = functools.reduce(lambda acc, m: [value for value in acc if value in m], members, members[0])
    count += len(group_ans)
print(count)


