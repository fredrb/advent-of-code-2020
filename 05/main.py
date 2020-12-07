
# high = 0
# for t in [t.strip() for t in open('input.txt').readlines()]:
#   (r,c) = t[:7].replace('F','0').replace('B','1'), t[7:].replace('L','0').replace('R','1')
#   seat_id = int(r,base=2) * 8 + int(c,base=2)
#   high = seat_id if seat_id > high else high
# print(high)

# T: 9m

seats = [False for i in range(0,1024)]
for t in [t.strip() for t in open('input.txt').readlines()]:
  (r,c) = t[:7].replace('F','0').replace('B','1'), t[7:].replace('L','0').replace('R','1')
  seat_id = int(r,base=2) * 8 + int(c,base=2)
  seats[seat_id] = True

for s_id in range(1, 1023):
  if not seats[s_id] and seats[s_id+1] and seats[s_id-1]:
    print(s_id)


