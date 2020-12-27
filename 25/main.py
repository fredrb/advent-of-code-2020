# Example:
# card_key = 5764801
# door_key = 17807724

card_key = 6929599
door_key = 2448427

def break_enc(enc):
  loop = 0
  n = 1
  # for loop in range(1, 10000):
  while n != enc:
    loop += 1
    n = pow(7, loop, 20201227)
  return (n, loop)

(_, card_loop) = break_enc(card_key)
(_, door_loop) = break_enc(door_key)

print(card_loop)
print(door_loop)

a = pow(card_key, door_loop, 20201227)
b = pow(door_key, card_loop, 20201227)

print(a)
print(b)