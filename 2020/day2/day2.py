import os

def getComponents(entry):
  limits = [int(x) for x in entry[0].split("-")]
  char = entry[1].strip(":")
  password = entry[2]
  return limits, char, password

def part1(entries):
  valid = 0
  for entry in entries:
    limits, char, password = getComponents(entry)
    count = password.count(char)
    if count >= limits[0] and count <= limits[1]:
      valid += 1
  return valid

def part2(entries):
  valid = 0
  for entry in entries:
    limits, char, password = getComponents(entry)
    pos = [int(x)-1 for x in limits]
    if (password[pos[0]] == char and password[pos[1]] != char) or (password[pos[0]] != char and password[pos[1]] == char):
      valid += 1
  return valid

if __name__ == "__main__":
  here = os.path.dirname(os.path.abspath(__file__))
  filename = os.path.join(here, 'input')

  entries = [line.split() for line in open(filename, 'r')]
  print("Part1:", part1(entries))
  print("Part2:", part2(entries))