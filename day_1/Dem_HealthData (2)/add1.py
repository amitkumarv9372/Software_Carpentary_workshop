import sys

accumulator = 0
for line in sys.stdin:
    accumulator = int(line) + accumulator
print(accumulator)