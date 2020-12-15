import os

def part1(rows: list):
  for i, res in enumerate(rows):
    if(i < 25): continue
    valid = False
    nums = rows[i-25:i]
    for n1 in nums:
      if (res - n1) in nums:
        valid = True
    if valid == False:
      return res

def part2(rows: list):
  i, t = 500, 10884537
  for p1, _ in enumerate(rows):
    for p2 in range(p1+1, i):
      subset = rows[p1:p2+1]
      if t == sum(subset):
        return min(subset)+max(subset)

if __name__ == "__main__":
  here = os.path.dirname(os.path.abspath(__file__))
  filename = os.path.join(here, 'input')

  rows = [int(line.strip('\n')) for line in open(filename, 'r')]
  print("Part1:", part1(rows))
  print("Part2:", part2(rows))