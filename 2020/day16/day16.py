import os
import copy
from numpy import prod

def getSections(rows:list):
  section, myTicket, tickets, rules = 0, '', [], {}
  for r in rows:
    if r == '':
      section += 1
    else:
      if section == 0:
        name = r[:r.index(':')]
        rule = r[r.index(':')+1:].strip()
        parts = [[int(x) for x in p.split('-')] for p in rule.split(' or ')]
        rules[name] = tuple(parts)
      elif section == 1:
        if 'your ticket' not in r:
          myTicket = [int(x) for x in r.split(',')]
      elif section == 2:
        if 'nearby tickets' not in r:
          t = [int(x) for x in r.split(',')]
          tickets.append(t)
  return (myTicket, tickets, rules)

def part1(rows:list):
  myTicket, tickets, rules = getSections(rows)
  invalidNums, validTickets = [], []
  for t in tickets:
    validTicket = True
    rulesCopy = copy.deepcopy(rules)
    for n in t:
      valid = False
      for _, rule in rulesCopy.items():
        (mi1, ma1), (mi2, ma2) = rule
        if (mi1 <= n and n <= ma1) or (mi2 <= n and n <= ma2):
          valid = True 
          break
      if not valid:
        validTicket = False
        invalidNums.append(n) 
        break
    if validTicket:
      validTickets.append(t)
  return (invalidNums, validTickets, myTicket, rules)

def part2(tickets:list, rules:dict, myTicket:list):
  # Find rules matched per column
  colRules = {}
  for i in range(0, len(tickets[0])):
    col = [t[i] for t in tickets]
    for name, rule in rules.items():
      (mi1, ma1), (mi2, ma2) = rule
      ruleBroken = False
      for n in col:
        if ((mi1 <= n and n <= ma1) or (mi2 <= n and n <= ma2)):
          continue
        else:
          ruleBroken = True   
      if not ruleBroken:
        if colRules.get(i) == None:
          colRules[i] = [name]
        else:
          colRules[i].append(name)
  #  Reduce only one matched rule per col by assigning rule to col if it is the only rule matched
  solved = []
  while(True):
    for x, currRules in colRules.items():
      rule = currRules[0]
      if len(currRules) == 1 and rule not in solved:
        for y, compareRules in colRules.items():
          if x != y and rule in compareRules:
            colRules[y].remove(rule)
        solved.append(rule)
    if len(solved) == len(rules):
      break
  # Get cols with 'departure' in ruleName and compute product from vals in myTicket
  depCols =[i for i, name in colRules.items() if 'departure' in name[0]]
  depVals = [v for i, v in enumerate(myTicket) if i in depCols]
  return prod(depVals)

if __name__ == "__main__":
  here = os.path.dirname(os.path.abspath(__file__))
  filename = os.path.join(here, 'input')
  rows = [line.strip('\n') for line in open(filename, 'r')]
  
  invalidNums, validTickets, myTicket, rules = part1(rows)
  print("Part1:", sum(invalidNums))
  print("Part2:", part2(validTickets, rules, myTicket))
