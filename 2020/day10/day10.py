import os

def part1(rows: list):
  rows.sort()
  diffs = {1:0,2:0,3:0}
  for i in range(1, len(rows)):
    d = rows[i] - rows[i-1]
    diffs[d] += 1
  return diffs[1] * diffs[3]

def part2(rows:list):
  rows.sort()

  graph = {}
  for r in rows:
    valid = []
    if r+1 in rows:
      valid.append(r+1)
    if r+2 in rows:
      valid.append(r+2)
    if r+3 in rows:
      valid.append(r+3)
    graph[r] = valid

  solution = {0:1}
  for key,value in graph.items():
    if value == []:
      break
    for val in value:
      if val in solution.keys():
        solution[val]+=solution[key]
      else:
        solution[val]=solution[key]
    
  return solution[rows[-1]]

if __name__ == "__main__":
  here = os.path.dirname(os.path.abspath(__file__))
  filename = os.path.join(here, 'input')

  rows = [int(line.strip('\n')) for line in open(filename, 'r')]
  rows.append(0) # charging outlet
  rows.append(max(rows)+3) # device adapter

  print("Part1:", part1(rows))
  print("Part2:", part2(rows))