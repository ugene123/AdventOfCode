import os

def part1(total, entries):
  for entry1 in entries:
    entry2 = total - entry1
    if entry2 in entries:
      return entry1 * entry2

def part2(total, entries):
  for entry1 in entries:
    remainder = total - entry1
    for entry2 in entries: 
      entry3 = remainder - entry2 
      if entry3 in entries: 
        return entry1 * entry2 * entry3

if __name__ == "__main__":
  here = os.path.dirname(os.path.abspath(__file__))
  filename = os.path.join(here, 'input')
  entries = set([int(line.strip('\n')) for line in open(filename, 'r')])
  print("Part1:", part1(2020, entries))
  print("Part2:", part2(2020, entries))