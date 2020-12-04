import re

def test_property(n, v) -> bool:
    return {
        'byr': (lambda v: 1920 <= int(v) <= 2020),
        'iyr': (lambda v: 2010 <= int(v) <= 2020),
        'eyr': (lambda v: 2020 <= int(v) <= 2030),
        'hgt': (lambda v: ({
                'cm': (lambda v: 150 <= int(v[:len(v)-2]) <= 193),
                'in': (lambda v: 59 <= int(v[:len(v)-2]) <= 76)
            }.get(v[len(v)-2:]) or (lambda v: False))(v)),
        'hcl': (lambda v: re.match('^\#[a-f0-9]{6}$', v) is not None),
        'ecl': (lambda v: ['amb','blu','brn','gry','grn','hzl','oth'].count(v) > 0),
        'pid': (lambda v: len(v) == 9),
        'cid': (lambda v: True)
    }.get(n)(v)

count = 0
for record in [x.strip().replace('\n', ' ').split(' ') for x in open('input.txt').read().split('\n\n')]:
    p = {'byr': 0, 'iyr': 0, 'eyr': 0, 'hgt': 0, 'hcl': 0, 'ecl': 0, 'pid': 0, 'cid': 1}
    for prop in record:
        (n, v) = prop.split(':')
        p[n] = v if test_property(n, v) else 0
    count += 1 if len(list(filter(lambda x: x == 0, p.values()))) == 0 else 0
print(count)


# PART 1:
# count = 0
# for record in [x.strip().replace('\n', ' ').split(' ') for x in open('input.txt').read().replace('\n\n','||').split('||')]:
#     p = {'byr': 0, 'iyr': 0, 'eyr': 0, 'hgt': 0, 'hcl': 0, 'ecl': 0, 'pid': 0, 'cid': 1}
#     for prop in record:
#         (n, _) = prop.split(':')
#         p[n] = 1
#     count += 1 if len(list(filter(lambda x: x == 0, p.values()))) == 0 else 0
# print(count)