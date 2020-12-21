import re

(section1, section2) = open('input.txt').read().split('\n\n')
rules = {}

def evaluate_formula(fid):
  if isinstance(rules.get(fid), str):
    return rules.get(fid)
  if fid == 8:
    regex = '(%s)+' % evaluate_formula(42)
  elif fid == 11:
    r42 = evaluate_formula(42)
    r31 = evaluate_formula(31)
    regex = '('
    regex += '|'.join(['((%s){%s}(%s){%s})' % (r42, i, r31, i) for i in range(1,100)])
    regex += ')'
  else:
    regex = '('
    regex += '|'.join([''.join([evaluate_formula(r) for r in opt]) for opt in rules.get(fid)])
    regex += ')'
  rules[fid] = regex
  return regex

for rule in [l.split(': ') for l in section1.split('\n')]:
  (rule_id, formula) = rule
  if formula == '"a"' or formula == '"b"':
    rules[int(rule_id)] = formula.replace('"',"")
  else:
    rules[int(rule_id)] = [[int(n) for n in f.strip().split(' ')] for f in formula.split('|')]
# print(rules)
zero_rule = evaluate_formula(0)
# print(zero_rule)
# zero_regex = re.compile(zero_rule, "g")

c = 0
for l in section2.split('\n'):
  if re.fullmatch(zero_rule, l):
    print(l)
    c += 1
print(c)