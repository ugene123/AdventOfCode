import os

def getGroups(rows: list):
  res = [[]]
  for i in rows:
    if not i:
      res.append([])
    else:
      res[-1].append(i)
  return res

def getUniqueAnswers(answers: list):
  unique = set()
  for a in answers:
    for char in a:
      unique.add(char)
  return len(unique)

def getAllAnswers(answers: list):
  res = {}
  for a in answers:
    for char in a:
      res[char] = res[char]+1 if res.get(char) != None else 1
  return sum([(1 if res.get(k) == len(answers) else 0) for k in res.keys()])

def part1(groups: list):
  return sum([getUniqueAnswers(g) for g in groups])

def part2(groups: list):
  return sum([getAllAnswers(g) for g in groups])

if __name__ == "__main__":
  here = os.path.dirname(os.path.abspath(__file__))
  filename = os.path.join(here, 'input')

  groups = getGroups([line.strip('\n') for line in open(filename, 'r')])
  print("Part1:", part1(groups))
  print("Part2:", part2(groups))