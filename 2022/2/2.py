input = open('input.txt').read().splitlines()

winPoints = 6
drawPoints = 3
losePoints = 0

throwPoints = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
toWin = {"A": "Y", "B": "Z", "C": "X"}
toLose = {"A": "Z", "B": "X", "C": "Y"}

def part1():
  myPoints = 0
  for line in input:
    myThrow = line.split()[1]
    if line in ["A Y", "B Z", "C X"]: #win
      myPoints += (winPoints + throwPoints[myThrow])
    elif line in ["A Z", "B X", "C Y"]: #lose
      myPoints += (losePoints + throwPoints[myThrow])
    else: #draw
      myPoints += (drawPoints + throwPoints[myThrow])
  return myPoints

def part2():
  myPoints = 0
  for line in input:
    theirThrow, matchStatus = line.split()
    if matchStatus == "Z": #win
      myPoints += (winPoints + throwPoints[toWin[theirThrow]])
    elif matchStatus == "X": #lose
      myPoints += (losePoints + throwPoints[toLose[theirThrow]])
    else: #draw
      myPoints += (drawPoints + throwPoints[theirThrow])
  return myPoints

print("Part 1:", part1())
print("Part 2:", part2())