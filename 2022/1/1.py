input = open('input.txt').read().splitlines()

elvesCalories = []
currentElfCalories = 0

for line in input:
  if line == "":
    elvesCalories.append(currentElfCalories)
    currentElfCalories = 0
  else:
    currentElfCalories += int(line)
elvesCalories.sort()

print("Part 1:", (elvesCalories[-1]))
print("Part 2:", sum(elvesCalories[-3:]))