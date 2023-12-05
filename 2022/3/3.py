input = open('input.txt').read().splitlines()

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def part1():
  prioritySum = 0
  for sack in input:
    compartment1, compartment2 = sack[:len(sack)//2], sack[len(sack)//2:]
    for item in compartment1:
      if item in compartment2:
        prioritySum += letters.index(item) + 1
        break;
  return prioritySum

def part2():
  elfGroupSacks = []
  prioritySum = 0
  for sack in input:
    elfGroupSacks.append(sack)
    if len(elfGroupSacks) == 3:
      possibleBadges = letters
      for sack in elfGroupSacks:
        for possibleBadge in possibleBadges:
          if possibleBadge not in sack:
            possibleBadges = possibleBadges.replace(possibleBadge, "")
      prioritySum += letters.index(possibleBadges) + 1
      elfGroupSacks = []
  return prioritySum

print("Part 1:", part1())
print("Part 2:", part2())