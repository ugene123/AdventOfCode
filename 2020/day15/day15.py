import os

def addToPos(pos:dict, key:int, index:int):
  if pos.get(key) == None:
    pos[key] = [index]
  else:
    last = pos[key][-1]
    pos[key] = [last, index]

def playGame(nums:list, turns:int):
  pos, end, last = {}, len(nums), nums[-1]
  for t in range(0, turns):
    if t < end:
      addToPos(pos, nums[t], t)
    else:
      if len(pos[last]) == 1:
        addToPos(pos, 0, t)
        last = 0
      else:
        res = pos[last][-1] - pos[last][-2]
        addToPos(pos, res, t)
        last = res
  return last

if __name__ == "__main__":
  here = os.path.dirname(os.path.abspath(__file__))
  filename = os.path.join(here, 'input')
  nums = [0,5,4,1,10,14,7]
  print("Part1:", playGame(nums, 2020))
  print("Part2:", playGame(nums, 30000000))
