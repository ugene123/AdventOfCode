import os

def getComponents(entry):
  limits = [int(x) for x in entry[0].split("-")]
  char = entry[1].strip(":")
  password = entry[2]
  return limits[0], limits[1], char, password

def part1(entries):
  valid = 0
  for entry in entries:
    lmin, lmax, char, password = getComponents(entry)
    count = password.count(char)
    if count >= lmin and count <= lmax:
      valid += 1
  return valid

def part2(entries):
  valid = 0
  for entry in entries:
    lmin, lmax, char, password = getComponents(entry)
    pos1 = lmin - 1
    pos2 = lmax - 1
    if (password[pos1] == char and password[pos2] != char) or (password[pos1] != char and password[pos2] == char):
      valid += 1
  return valid

if __name__ == "__main__":
  here = os.path.dirname(os.path.abspath(__file__))
  filename = os.path.join(here, 'input')

  entries = [line.split() for line in open(filename, 'r')]
  print("Part1:", part1(entries))
  print("Part2:", part2(entries))