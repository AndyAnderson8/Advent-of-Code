import copy
input = open('input.txt').read().splitlines()

cratePositions = [
  ["B", "S", "V", "Z", "G", "P", "W"],
  ["J", "V", "B", "C", "Z", "F"],
  ["V", "L", "M", "H", "N", "Z", "D", "C"],
  ["L", "D", "M", "Z", "P", "F", "J", "B"],
  ["V", "F", "C", "G", "J", "B", "Q", "H"],
  ["G", "F", "Q", "T", "S", "L", "B"],
  ["L", "G", "C", "Z", "V"],
  ["N", "L", "G"],
  ["J", "F", "H", "C"]
]

stackSets = [copy.deepcopy(cratePositions), copy.deepcopy(cratePositions)]
for line in input:
  crateCount = int(line.split("move ")[1].split(" from")[0])
  originStack = int(line.split("from ")[1].split(" to")[0]) - 1
  destinationStack = int(line.split("to ")[1]) - 1
  for i in range(crateCount):
    stackSets[0][destinationStack].append(stackSets[0][originStack].pop())
    stackSets[1][destinationStack].append(stackSets[1][originStack].pop(len(stackSets[1][originStack]) + i - crateCount))
for i, stacks in enumerate(stackSets):
  topCrates = ""
  for j in range(len(stacks)):
      topCrates += stacks[j][-1]
  print("Part", str(i + 1) + ":", topCrates)