ins = [(i.split(' ')[0], int(i.split(' ')[1])) for i in open('input.txt').readlines()]

class Machine:
  def __init__(self, ins):
    self.mem = ins
    self.acc_reg = 0
    self.pointer = -1
    self.mem_track = [False for i in ins]

  def acc(self, v):
    self.acc_reg += v

  def nop(self, v):
    pass

  def jmp(self, v):
    self.pointer += (v-1)

  def op_exec(self, op):
    return {
      'acc': self.acc,
      'jmp': self.jmp,
      'nop': self.nop
    }[op]

  def run(self):
    while True:
      self.pointer += 1
      if self.pointer == len(self.mem):
        return True
      if self.mem_track[self.pointer]:
        return False
      self.mem_track[self.pointer] = True
      code = self.mem[self.pointer]
      self.op_exec(code[0])(code[1])

flip_instructions = []
for i in range(0, len(ins)):
  if ins[i][0] == 'nop':
    flip_instructions.append((i, 'jmp'))
  if ins[i][0] == 'jmp':
    flip_instructions.append((i, 'nop'))

for n in flip_instructions:
  new_ins = ins.copy()
  new_ins[n[0]] = (n[1], new_ins[n[0]][1])
  m = Machine(new_ins)
  if m.run():
    print("Finished execution! Acc: %s" % m.acc_reg)
    break