import os

class Ship:
  def __init__(self):
    self.directions = ['N','E','S','W']
    self.facing = 'E'
    self.x, self.y = 0, 0 
    self.wX, self.wY = 10, 1

  def getLongDirection(self, n):
    return 'N' if n > 0 else 'S' 

  def getLatDirection(self, n):
    return 'E' if n > 0 else 'W' 

  def followInstruction(self, cmd):
    inst, n = cmd[0], int(cmd[1:])
    if inst in ['F','N','E','S','W']:
      self.moveShip(inst, n)
    if inst in ['R','L']:
      self.turnShip(inst, n)

  def followWaypoint(self, cmd):
    inst, n = cmd[0], int(cmd[1:])
    if inst == 'F':
      d1, d2 = self.getLongDirection(self.wY), self.getLatDirection(self.wX)
      self.moveShip(d1, abs(self.wY*n))
      self.moveShip(d2, abs(self.wX*n))
    if inst in ['N','E','S','W']:
      self.moveWaypoint(inst, n)
    if inst in ['R','L']:
      self.turnWaypoint(inst, n)

  def moveWaypoint(self, dir, n):
    if dir == 'N':
      self.wY += n
    elif dir== 'E':
      self.wX += n
    elif dir == 'S':
      self.wY -= n
    elif dir == 'W':
      self.wX -= n

  def turnWaypoint(self, dir, deg):
    tempX, tempY = abs(self.wX), abs(self.wY)
    curX = self.getLatDirection(self.wX)
    curY = self.getLongDirection(self.wY)
    
    m = (deg // 90) if dir == 'R' else (-deg//90)
    dir1 = self.directions[((self.directions.index(curX)+m) % 4)]
    dir2 = self.directions[((self.directions.index(curY)+m) % 4)]

    self.updateWaypoint(dir1, tempX)
    self.updateWaypoint(dir2, tempY)

  def updateWaypoint(self, dir, n):
    if dir == 'N':
      self.wY = n
    elif dir == 'E':
      self.wX = n
    elif dir == 'S':
      self.wY = -n
    elif dir == 'W':
      self.wX = -n

  def turnShip(self, dir, deg):
    m = (deg//90) if dir == 'R' else (-deg//90)
    i = ((self.directions.index(self.facing)) + m) % 4
    self.facing = self.directions[i]

  def moveShip(self, dir, n):
    if dir == 'N':
      self.y += n
    elif dir== 'E':
      self.x += n
    elif dir == 'S':
      self.y -= n
    elif dir == 'W':
      self.x -= n
    elif dir == 'F':
      self.moveShip(self.facing, n)

  def ManhattanDistance(self): 
    return abs(self.x) + abs(self.y)
      
def part1(rows: list):
  ship = Ship()
  [ship.followInstruction(r) for r in rows]
  return ship.ManhattanDistance()

def part2(rows: list):
  ship = Ship()
  [ship.followWaypoint(r) for r in rows]
  return ship.ManhattanDistance()

if __name__ == "__main__":
  here = os.path.dirname(os.path.abspath(__file__))
  filename = os.path.join(here, 'input')

  rows = [line.strip('\n') for line in open(filename, 'r')]
  print("Part1:", part1(rows))
  print("Part2:", part2(rows))