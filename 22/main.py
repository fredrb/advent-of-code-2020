(deck1, deck2) = [d.split('\n')[1:] for d in open('example.txt').read().split('\n\n')]

deck1 = list(reversed([int(i) for i in deck1]))
deck2 = list(reversed([int(i) for i in deck2]))

class GameRound:
  def __init__(self, d1, d2):
    self.d1 = d1
    self.d2 = d2
    self.history = {}

  def has_history_state(self):
    s = ','.join([str(i) for i in self.d1]) + ','.join([str(i) for i in self.d2])
    if self.history.get(s):
      return True
    self.history[s] = True
    return False

  def play(self):
    while not any([len(self.d1) == 0, len(self.d2) == 0]):
      if self.has_history_state():
        return (1, self.d1)
      (a, b) = (self.d1.pop(), self.d2.pop())
      if (len(self.d1) >= a and len(self.d2) >= b):
        (round_winner, _) = GameRound(self.d1[-a:], self.d2[-b:]).play()
      elif a > b:
        round_winner = 1
      else:
        round_winner = 2
      if round_winner == 1:
        self.d1 = [b, a] + self.d1
      else:
        self.d2 = [a, b] + self.d2
    if len(self.d1) == 0:
      return (2, self.d2)
    else:
      return (1, self.d1)

(_, winner) = GameRound(deck1, deck2).play()

score = 0
for i in range(1, len(winner)+1):
  score += winner[i-1]*i

print(score)