import os

def getPosition(ticket: str, total: int, start: int, end: int, frontHalf: str, backHalf: str):
  min, mid, max = 0, None, total-1
  for i in range(start, end):
    mid = (min + max) // 2
    if ticket[i] == frontHalf:
      max = mid
    if ticket[i] == backHalf:
      mid += 1
      min = mid
  return mid

def getSeatIds(tickets):
  seatIds = []
  for t in tickets:
    row = getPosition(t, 128, 0, 7, 'F', 'B')
    col = getPosition(t, 8, 7, 10, 'L', 'R')
    seatIds.append(row * 8 + col)
  return seatIds

def part1(tickets):
  seatIds = getSeatIds(tickets)
  return max(seatIds)

def part2(tickets):
  seatIds = getSeatIds(tickets)
  for id in seatIds:
    if id+1 not in seatIds and id+2 in seatIds:
      return id+1
    if id-1 not in seatIds and id-2 in seatIds:
      return id-1

if __name__ == "__main__":
  here = os.path.dirname(os.path.abspath(__file__))
  filename = os.path.join(here, 'input')

  rows = [line.strip('\n') for line in open(filename, 'r')]
  print("Part1:", part1(rows))
  print("Part2:", part2(rows))
