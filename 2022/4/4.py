input = open('input.txt').read().splitlines()

def part1():
  fullyContainedSections = 0;
  for line in input:
    sectionRanges = []
    for sectionRange in line.split(","):
      startingSection, endingSection = sectionRange.split("-")
      sectionRange = ""
      for j in range(int(endingSection) - int(startingSection) + 1):
        sectionRange += " " + str(j + int(startingSection)) + ","
      sectionRanges.append(sectionRange)
    if sectionRanges[0] in sectionRanges[1] or sectionRanges[1] in sectionRanges[0]:
      fullyContainedSections += 1
  return fullyContainedSections

def part2():
  overlappingSections = 0
  for line in input:
    sectionRanges = []
    for sectionRange in line.split(","):
      startingSection, endingSection = sectionRange.split("-")
      sectionRange = []
      for j in range(int(endingSection) - int(startingSection) + 1):
        sectionRange.append(j + int(startingSection))
      sectionRanges.append(sectionRange)
    for section in sectionRanges[0]:
      if section in sectionRanges[1]:
        overlappingSections += 1
        break
  return overlappingSections

print("Part 1:", part1())
print("Part 2:", part2())