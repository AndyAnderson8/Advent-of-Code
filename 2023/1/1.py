import re

def parseInput(path):
  return open(path).read().splitlines()

def partOne(input):
  sum = 0
  for line in input:
    nums = re.sub("[^0-9]", "", line)
    num1 = nums[0]
    num2 = nums[len(nums) - 1]
    sum += int(num1 + num2)
  return sum

def partTwo(input):
  sum = 0
  numDict = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
  }

  for line in input:
    localSum = ""

    #find first num
    found = False
    startChar = 0
    while not found:
      char = line[startChar]
      if char in "1234567890": #check for num char
        localSum += char
        found = True
      else: #check for num word
        for word, num in numDict.items():
          substring = line[startChar:len(word) + startChar]
          if substring == word:
            localSum += num
            found = True
      startChar += 1

    #find last num
    found = False
    endChar = 0
    while not found:
      char = line[len(line) - endChar - 1]
      if char in "1234567890": #check for num char
        localSum += char
        found = True
      else: #check for num word
        for word, num in numDict.items():
          substring = line[len(line) - len(word) - endChar:len(line) - endChar]
          if substring == word:
            localSum += num
            found = True
      endChar += 1

    sum += int(localSum)
    
  return sum

def main():
  input = parseInput("input.txt")
  print(f"Part 1: {partOne(input)}")
  print(f"Part 2: {partTwo(input)}")

main()