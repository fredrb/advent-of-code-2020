# puzzle = [(r[0].strip(), [t.strip().replace('bags','').replace('bag','').replace('.','').strip()
#     for t in r[1].split(',')]) 
#     for r in [l.strip().split('bags contain') for l in open('input.txt').readlines()]]

# def outter_rules(puzzle: list, t: str):
#     return list(filter(lambda x: list(filter(lambda y: y[2:] == t, x[1])), puzzle))

# possible_colors = []
# colors = ['shiny gold']
# while len(colors) > 0:
#     next_colors = []
#     [next_colors.extend(outter_rules(puzzle, c)) for c in colors]
#     colors = list(dict.fromkeys([n[0] for n in next_colors]))
#     possible_colors.extend(colors)
# print(len(possible_colors))
# print(len(dict.fromkeys(possible_colors).keys()))

# part 2

import functools

puzzle = [(r[0].strip(), [t.strip().replace('bags','').replace('bag','').replace('.','').strip()
    for t in r[1].split(',')]) 
    for r in [l.strip().split('bags contain') for l in open('input.txt').readlines()]]

def inner_rules(puzzle: list, t: str):
    return list(filter(lambda x: x[0] == t, puzzle))

def calc(color: str):
    rule = [item for sub in [r[1] for r in inner_rules(puzzle, color)] for item in sub]
    rule = [(int(item[:2].strip()), item[2:]) for item in list(filter(lambda r: r != 'no other', rule))]
    return 0 if len(rule) == 0 else functools.reduce(lambda acc,x: acc + (x[0]) + (x[0]) * calc(x[1]), rule, 0)

print(calc('shiny gold'))

