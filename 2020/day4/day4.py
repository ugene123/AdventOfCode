import os
import re

def containsReqs(psswrd: str):
  required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
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
      if 'cm' in value:
        if not (int(value.strip('cm')) >= 150 and int(value.strip('cm')) <= 190):
          return False
      elif 'in' in value:
        if not (int(value.strip('in')) >= 59 and int(value.strip('in')) <= 76):
          return False
      else:
        return False
    if key == 'hcl':
      if re.match('^#([abcdef0123456789]{6})', value) == None:
        return False
    if key == 'ecl':
      if re.match('^(amb|blu|brn|gry|grn|hzl|oth)$', value) == None:
        return False
    if key == 'pid':
      if re.match('^\d{9}$', value) == None:
        return False
  return True

def getPasswords(rows: list):
  indexes = []
  start = 0
  for i, row in enumerate(rows):
    if row == '\n':
      indexes.append((start, i - 1))
      start = i + 1
  return indexes

def part1(rows: list):
  valid = 0
  passIndexes = getPasswords(rows)
  for start, end in passIndexes:
    psswrd = ""
    for i in range(start, end + 1):
      psswrd += ' ' + rows[i].replace('\n', ' ')
    if containsReqs(psswrd):
      valid += 1
  return valid

def part2(rows: list):
  valid = 0
  passIndexes = getPasswords(rows)
  for start, end in passIndexes:
    psswrd = ""
    for i in range(start, end + 1):
      psswrd += ' ' + rows[i].replace('\n', ' ')
    if isValid(psswrd):
      valid += 1
  return valid

if __name__ == "__main__":
  here = os.path.dirname(os.path.abspath(__file__))
  filename = os.path.join(here, 'input')

  
  rows = [line for line in open(filename, 'r')]
  
  print("Part1:", part1(rows))
  print("Part2:", part2(rows))
