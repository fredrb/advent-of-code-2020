# Part 1:
# ins = [(i[0], int(i[1:])) for i in open('input.txt').readlines()]

# pos = (0, 0)
# current_dir = 1

# dirmap = {
#   0: 'N', 1: 'E', 2: 'S', 3: 'W'
# }

# direction = {
#   'N': (0,1),
#   'S': (0,-1),
#   'W': (1,0),
#   'E': (-1,0)
# }

# for (i,v) in ins:
#   if i in ['N', 'S', 'E', 'W']:
#     pos = (direction[i][0]*v + pos[0], direction[i][1]*v + pos[1])
#   if i in ['R', 'L']:
#     delta = v//90
#     current_dir = (current_dir + delta if i == 'R' else current_dir - delta)%4
#   if i == 'F':
#     pos = (direction[dirmap[current_dir]][0]*v + pos[0], direction[dirmap[current_dir]][1]*v + pos[1])
# print(abs(pos[0])+abs(pos[1]))

# Part 2:

ins = [(i[0], int(i[1:])) for i in open('input.txt').readlines()]

pos = (0, 0)
waypoint = (10, 1)
current_dir = 1

def make_rotate_array(p):
  arr = [0, 0, 0, 0]
  arr[1 if p[0] > 0 else 3] = abs(p[0])
  arr[0 if p[1] > 0 else 2] = abs(p[1])
  return arr

def rotate_dir(p, d):
  arr = make_rotate_array(p)
  if d == 'R':
    carry = arr[len(arr)-1]
    arr = [carry] + arr[:len(arr)-1]
  else:
    carry = arr[0]
    arr = arr[1:] + [carry]
  return (arr[1] or -arr[3], arr[0] or -arr[2])

direction = {
  'N': (0,1),
  'S': (0,-1),
  'W': (-1,0),
  'E': (1,0)
}

for (i,v) in ins:
  if i in ['N', 'S', 'E', 'W']:
    waypoint = (direction[i][0]*v + waypoint[0], direction[i][1]*v + waypoint[1])
  if i in ['R', 'L']:
    delta = v//90
    for _ in range(0, delta):
      waypoint = rotate_dir(waypoint, i)
  if i == 'F':
    for _ in range(0, v):
      pos = (pos[0]+waypoint[0], pos[1]+waypoint[1])
print(abs(pos[0])+abs(pos[1]))