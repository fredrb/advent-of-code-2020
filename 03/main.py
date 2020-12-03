tree_map = [l.strip() for l in open('input.txt').readlines()]
tc = 1
for slope in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    p = (0, 0)
    _tc = 0
    while p[1] < len(tree_map):
        if tree_map[p[1]][p[0]] == '#':
            _tc += 1
        p = ((p[0]+slope[0])%len(tree_map[0]), p[1] + slope[1])
    tc *= _tc
print(tc)