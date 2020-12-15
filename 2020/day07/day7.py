import os

def getRules(rows: list):
  rules = {}
  for r in rows:
    color, bags = r.split('contain')
    color = color.replace('bags', '').strip()
    bags = [] if 'no other bags.' in bags else bags.strip('.').split(', ')
    rules[color] = [b.replace('bags','').replace('bag','').strip() for b in bags]
  return rules

def getBagsWithColor(rules: list, color: str):
  bags = []
  for k in rules.keys():
    for b in rules[k]:
      if color in b:
        bags.append(k)
  return bags

def getCount(bag: list, rules: dict):
  total = 1
  bags = rules[bag]
  for b in bags:
    n, adj, color = b.split(' ')
    for _ in range(0, int(n)):
      total += getCount(f'{adj} {color}', rules)
  return total

def part1(rules: dict, search: str):
  unscanned = getBagsWithColor(rules, search)
  scanned = []
  while len(unscanned) > 0:
    curr = unscanned.pop(0)
    morebags = getBagsWithColor(rules, curr)
    if len(morebags) > 0: 
      unscanned.extend(morebags)
    scanned.append(curr)
  return len(set(scanned))

def part2(rules: dict, search: str):
  return getCount('shiny gold', rules) - 1

if __name__ == "__main__":
  here = os.path.dirname(os.path.abspath(__file__))
  filename = os.path.join(here, 'input')

  rows = [line.strip('\n') for line in open(filename, 'r')]
  rules = getRules(rows)
  print("Part1:", part1(rules, 'shiny gold'))
  print("Part2:", part2(rules, 'shiny gold'))