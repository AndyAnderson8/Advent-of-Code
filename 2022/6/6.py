input = open('input.txt').read()

def packetBeginningIndex(markerLength):
  for i in range(markerLength, len(input)):
    if len(set(input[i - markerLength:i])) == markerLength:
      return i

print("Part 1:", packetBeginningIndex(4))
print("Part 2:", packetBeginningIndex(14))