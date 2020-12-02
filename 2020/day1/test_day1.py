from day1 import part1, part2

total = 100
entries = set([10, 20, 70, 30])

def test_part1():
  result = part1(total, entries)
  assert result == 2100

def test_part2():
  result = part2(total, entries)
  assert result == 14000
