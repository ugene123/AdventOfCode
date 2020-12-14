import os
import math

def part1(rows:list):
  start, buses = int(rows[0]), [int(b) for b in rows[1].split(',') if b != 'x']
  d = {}
  for b in buses:
    first = math.ceil(start/b) * b
    d[b] = first
  e = min(d, key=d.get)
  return e * (d[e] - start)

def part2(rows:list):
  _, ids = int(rows[0]), [(int(b) if b != 'x' else b) for b in rows[1].split(',') ]
  buses = dict(zip(range(0, len(ids)), iter(ids)))
  time = 0
  iteration = 0 
  first = max([(n if n != 'x' else 0) for n in buses.values()])
  fIndex = None
  for k, v in buses.items():
    if v == first:
      fIndex = k
  while True:
    num = (time+fIndex) / int(first)
    if num.is_integer():
      for i, b in buses.items(): 
        if b == 'x': continue
        a = (time+i) / int(b)
        if not a.is_integer():
          break 
        else:
          if i == len(buses) - 1:
            return time
    time = (iteration*first)-fIndex
    iteration+=1
   
if __name__ == "__main__":
  here = os.path.dirname(os.path.abspath(__file__))
  filename = os.path.join(here, 'input')

  rows = [line.strip('\n') for line in open(filename, 'r')]
  print("Part1:", part1(rows))
  print("Part2:", part2(rows))