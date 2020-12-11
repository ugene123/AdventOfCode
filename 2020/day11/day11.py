import os
import copy

directions = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]

def getAdjacent(y, x, sMap):
  t, limX, limY = 0, len(sMap[0])-1, len(sMap)-1
  for dX, dY in directions:
    nX = x+dX
    nY = y+dY
    if nY < 0 or nX <0 or nX > limX or nY > limY:  
      continue
    if sMap[nY][nX] == '#':
      t += 1
  return t

def getVisible(y, x, sMap):
  t, limX, limY = 0, len(sMap[0])-1, len(sMap)-1
  for dX, dY in directions:
    nX = x+dX
    nY = y+dY
    while(True):
      if (nX < 0 or nY < 0) or (nX > limX or nY > limY):
        break
      c = sMap[nY][nX]
      if c == '#':
        t+=1
        break
      if c == 'L':
        break
      nX += dX
      nY += dY
  return t

def iterAdjacent(sMap):
  res = copy.deepcopy(sMap)
  for y, r in enumerate(sMap):
    for x, c in enumerate(r):
      if c != '.':
        adj = getAdjacent(y, x, sMap)
        if c == 'L' and adj == 0:
          res[y][x] = '#'
        if c == '#' and adj >= 4:
          res[y][x] = 'L'
  return res

def iterVisible(sMap):
  res = copy.deepcopy(sMap)
  for y, r in enumerate(sMap):
    for x, c in enumerate(r):
      if c != '.':
        v = getVisible(y, x, sMap)
        if c == 'L' and v == 0:
          res[y][x] = '#'
        if c == '#' and v >= 5:
          res[y][x] = 'L'
  return res

def getOccupied(sMap):
  return sum([sum([1 for c in r if c == '#']) for r in sMap])

def part1(sMap):
  map1 = sMap
  while(True):
    map2 = iterAdjacent(map1)
    if map1 == map2:
      return getOccupied(map1)
    else:
      map1 = map2

def part2(sMap):
  map1 = sMap
  while(True):
    map2 = iterVisible(map1)
    if map1 == map2:
      return getOccupied(map1)
    else:
      map1 = map2

if __name__ == "__main__":
  here = os.path.dirname(os.path.abspath(__file__))
  filename = os.path.join(here, 'input')

  sMap = [[char for char in (line.strip('\n'))] for line in open(filename, 'r')]
  print("Part1:", part1(sMap))
  print("Part2:", part2(sMap))
