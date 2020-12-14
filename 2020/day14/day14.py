import os

def part1(rows:list):
  mem, mask = {}, ''
  for r in rows:
    if r[0:4] == 'mask':
      mask = r[7:]
    elif r[0:3] == 'mem':
      loc, val = [int(x) for x in r.replace('mem[','').replace('] ','').split('=')]
      b = str(bin(val)).replace('0b', '')
      res = ''
      for i in range(1, 37):
        m = mask[-i]
        if m != 'X':
          res += m
        else:
          n = '0' if i > len(b) else b[-i]
          res += n
      mem[loc] = res[::-1]
  nums = [int(v, 2) for v in mem.values()]
  return sum(nums)

def part2(rows: list):
  mem, mask = {}, ''
  for r in rows:
    if r[0:4] == 'mask':
      mask = r[7:]
    elif r[0:3] == 'mem':
      loc, val = [int(x) for x in r.replace('mem[','').replace('] ','').split('=')]
      b = str(bin(loc)).replace('0b', '')
      res = ''
      for i in range(1, 37):
        m = mask[-i]
        if m == 'X' or m == '1':
          res += m
        elif m == '0':
          n = '0' if i > len(b) else b[-i]
          res += n
      res = res[::-1]
      x = sum([1 for c in res if c == 'X'])
      combos = []
      for i in range(0, 2**x):
        combo = list('0' * x)
        b = str(bin(i)).replace('0b', '')
        for i in range(1, x+1):
          combo[-i] = b[-i] if i <= len(b) else '0'
        combos.append(''.join(combo))
      xIndexes = [pos for pos, char in enumerate(res) if char == 'X'][::-1]
      for combo in combos:
        key = list(res)
        for i, xIndex in enumerate(xIndexes):
          key[xIndex] = combo[-i] if i < len(combo) else '0'
        key = int(''.join(key), 2)
        mem[key] = val
  return sum(mem.values())

if __name__ == "__main__":
  here = os.path.dirname(os.path.abspath(__file__))
  filename = os.path.join(here, 'input')

  rows = [line.strip('\n') for line in open(filename, 'r')]
  print("Part1:", part1(rows))
  print("Part2:", part2(rows))
