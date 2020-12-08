ins = [(i.split(' ')[0], int(i.split(' ')[1])) for i in open('input.txt').readlines()]

class Machine:
  def __init__(self, ins):
    self.mem = ins
    self.acc_reg = 0
    self.pointer = -1
    self.mem_track = [0 for i in ins]

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
      # print('Running [%s]%s' % (self.pointer, self.mem[self.pointer]))
      if self.mem_track[self.pointer] > 2:
        return False
      self.mem_track[self.pointer] += 1
      code = self.mem[self.pointer]
      self.op_exec(code[0])(code[1])

nop_instructions = []
jmp_instructions = []
for i in range(0, len(ins)):
  if ins[i][0] == 'nop':
    nop_instructions.append(i)
  if ins[i][0] == 'jmp':
    jmp_instructions.append(i)

for n in nop_instructions:
  new_ins = ins.copy()
  # print("Changing nop from addr %s" % n)
  new_ins[n] = ('jmp', new_ins[n][1])
  m = Machine(new_ins)
  if m.run():
    print("Finished execution! Acc: %s" % m.acc_reg)
    break

for j in jmp_instructions:
  new_ins = ins.copy()
  # print("Changing jmp from addr %s" % j)
  new_ins[j] = ('nop', new_ins[j][1])
  m = Machine(new_ins)
  if m.run():
    print("Finished execution! Acc: %s" % m.acc_reg)
    break

