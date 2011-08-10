orientations='NESW'

def rove(position, instructions):
  if instructions:
    instruction = instructions[0]
    if instruction == 'M':
      if position[2] % 4 < 2:
        position[position[2]%2] += 1
      else:
        position[position[2]%2] -= 1
    else:
      position[2] += [1,-1][instruction == 'R']

  return rove(position, instructions[1:]) if instructions else (position[1], position[0], orientations[position[2]%4])

board_size = raw_input()
try:
  while True:
    x, y, orientation = raw_input()[::2]
    print "%d %d %s" % rove(map(int, [y, x, orientations.find(orientation)]), raw_input())
except:1
