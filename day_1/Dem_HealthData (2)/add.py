import sys

accumulator = 0

for line in sys.std.in:
    accumulator = int(line) + accumulator

print accumulator