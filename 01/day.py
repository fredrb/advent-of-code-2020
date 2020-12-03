lines = open('input.txt').readlines()
t = list(map(lambda y: 2020-int(y), lines))
for l1 in lines:
    _t1 = list(filter(lambda x: x > 0, list(map(lambda y: y-int(l1), t))))
    for l2 in lines:
        _t2 = list(filter(lambda x: x == 0, list(map(lambda y: y-int(l2), _t1))))
        if len(_t2) > 0:
            print(int(l1)* int(l2)* (2020-int(l1)-int(l2)))
            break