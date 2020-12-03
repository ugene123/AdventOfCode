import os

def part1(rows: list, rowLength: int, over: int, down: int) -> int:
  lastX, lastY, trees = 0, 0, 0
  while lastY < len(rows):
    if rows[lastY][lastX] == '#':
      trees += 1
    lastX += over
    lastY += down
    if lastX > rowLength - 1:
      lastX -= rowLength 
  return trees

def part2(rows: list, rowLength: int, slopes: list) -> int:
  total = 1
  for x, y in slopes:
    total *= part1(rows, rowLength, x, y)
  return total

if __name__ == "__main__":
  here = os.path.dirname(os.path.abspath(__file__))
  filename = os.path.join(here, 'input')

  rows = [line.strip('\n') for line in open(filename, 'r')]
  rowLength = len(rows[0]) 
  print("Part1:", part1(rows, rowLength, 3, 1))

  slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
  print("Part2:", part2(rows, rowLength, slopes))