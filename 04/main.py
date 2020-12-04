import re

# PART 1:
# count = 0
# for record in [x.strip().replace('\n', ' ').split(' ') for x in open('input.txt').read().replace('\n\n','||').split('||')]:
#     p = {'byr': 0, 'iyr': 0, 'eyr': 0, 'hgt': 0, 'hcl': 0, 'ecl': 0, 'pid': 0, 'cid': 1}
#     for prop in record:
#         (n, _) = prop.split(':')
#         p[n] = 1
#     count += 1 if len(list(filter(lambda x: x == 0, p.values()))) == 0 else 0
# print(count)

def test_property(n, v) -> bool:
    if n == 'byr':
        return 1920 <= int(v) <= 2020
    if n == 'iyr':
        return 2010 <= int(v) <= 2020
    if n == 'eyr':
        return 2020 <= int(v) <= 2030
    if n == 'hgt':
        un = v[len(v)-2:]
        v = v.split(un)[0]
        if un == 'cm':
            return 150 <= int(v) <= 193
        elif un == 'in':
            return 59 <= int(v) <= 76
        else:
            return False
    if n == 'hcl':
        return re.match('^\#[a-f0-9]{6}$', v) is not None
    if n == 'ecl':
        return ['amb','blu','brn','gry','grn','hzl','oth'].count(v) > 0
    if n == 'pid':
        return len(v) == 9
    return True

# PART 2:
count = 0
for record in [x.strip().replace('\n', ' ').split(' ') for x in open('input.txt').read().replace('\n\n','||').split('||')]:
    p = {'byr': 0, 'iyr': 0, 'eyr': 0, 'hgt': 0, 'hcl': 0, 'ecl': 0, 'pid': 0, 'cid': 1}
    for prop in record:
        (n, v) = prop.split(':')
        p[n] = v if test_property(n, v) else 0
    count += 1 if len(list(filter(lambda x: x == 0, p.values()))) == 0 else 0
print(count)