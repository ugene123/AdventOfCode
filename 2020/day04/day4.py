import os
import re

required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

def getPasswords(rows: list):
  psswrds = []
  start = 0
  for i, row in enumerate(rows):
    if row == '\n':
      psswrd = getPassword(rows, start, i-1)
      psswrds.append(psswrd)
      start = i + 1
  return psswrds

def getPassword(rows, start, end):
  psswrd = ""
  for i in range(start, end + 1):
    psswrd += ' ' + rows[i].replace('\n', ' ')
  return psswrd

def containsReqs(psswrd: str):  
  for r in required:
    if r not in psswrd:
      return False
  return True

def isValid(psswrd: str):
  if not containsReqs(psswrd):
    return False
  parts = [x.split(':') for x in psswrd.split()]
  for key, value in parts:
    if key == 'byr':
      if not (int(value) >= 1920 and int(value) <= 2002):
        return False
    if key == 'iyr':
      if not (int(value) >= 2010 and int(value) <= 2020):
        return False
    if key == 'eyr':
      if not (int(value) >= 2020 and int(value) <= 2030):
        return False
    if key == 'hgt':
      if re.match('^\d{3}(cm)$', value ) != None:
        if not (int(value.strip('cm')) >= 150 and int(value.strip('cm')) <= 193):
          return False
      elif re.match('^\d{2}(in)$', value ) != None: 
        if not (int(value.strip('in')) >= 59 and int(value.strip('in')) <= 76):
          return False
      else:
        return False
    if key == 'hcl':
      if re.match('^#([abcdef0123456789]{6})$', value) == None:
        return False
    if key == 'ecl':
      if re.match('^(amb|blu|brn|gry|grn|hzl|oth)$', value) == None:
        return False
    if key == 'pid':
      if re.match('^\d{9}$', value) == None:
        return False
  return True

def part1(psswrds: list):
  valid = 0
  for p in psswrds:
    if containsReqs(p):
      valid += 1
  return valid

def part2(psswrds: list):
  valid = 0
  for p in psswrds:
    if isValid(p):
      valid += 1
  return valid

if __name__ == "__main__":
  here = os.path.dirname(os.path.abspath(__file__))
  filename = os.path.join(here, 'input')

  rows = [line for line in open(filename, 'r')]
  psswrds = getPasswords(rows)

  print("Part1:", part1(psswrds))
  print("Part2:", part2(psswrds))
