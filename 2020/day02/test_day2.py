from day2 import part1, part2

entries = [
  ["1-11", "a:", "abcdefgzzzzzzz"],
  ["2-10", "b:", "bbccddeeffggzz"],
  ["1-2", "y:", "abc"],
  ["1-10", "z:", "zday2tests"],
]

def test_part1():
  valid = part1(entries)
  assert valid == 3

def test_partt2():
  valid = part2(entries)
  assert valid == 3