import os

def getJmpNopRows(rows: list):
  res = []
  for i, r in enumerate(rows):
    op, _ = r.split()
    if op == 'jmp' or op == 'nop':
      res.append(i)
  return res
  
def part1(rows: list):
  ran, i, total = [], 0, 0
  while True:
    if i in ran: 
      return (total, False) # Inf loop, prg failed
    if i > len(rows)-1:
      return (total, True) # EOF, prg ran successfully
    ran.append(i)
    op, val = rows[i].split()
    if op == 'nop':
      i += 1
    elif op == 'acc':
      total += int(val)
      i += 1
    elif op == 'jmp':
      i += int(val)

def part2(rows: list):
  jmpNopRows = getJmpNopRows(rows)
  for i in jmpNopRows:
    cpy = rows.copy()
    op, _ = cpy[i].split()
    cpy[i] = cpy[i].replace(op, 'nop' if op == 'jmp' else 'jmp')
    t, success = part1(cpy)
    if(success): return t

if __name__ == "__main__":
  here = os.path.dirname(os.path.abspath(__file__))
  filename = os.path.join(here, 'input')

  rows = [line.strip('\n') for line in open(filename, 'r')]

  print("Part1:", part1(rows)[0])
  print("Part2:", part2(rows))