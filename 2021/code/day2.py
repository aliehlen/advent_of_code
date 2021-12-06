# data
data_file = "../data/day2.txt"

# read in list of integers
data = open(data_file, 'r').read().split("\n")

# PART A
# find total depth and horizontal position

horiz = 0
depth = 0

for command in data:
    value = int(command.split(" ")[1])

    if command.startswith('d'):
        depth += value
    elif command.startswith('u'):
        depth -= value
    elif command.startswith('f'):
        horiz += value

print(f"PART A: the product of coordinates is {horiz*depth}")

# PART B
# find total depth, horizontal position using more complex instructions

horiz = 0
depth = 0
aim = 0

for command in data:
    value = int(command.split(" ")[1])

    if command.startswith('d'):
        aim += value
    elif command.startswith('u'):
        aim -= value
    elif command.startswith('f'):
        horiz += value
        depth += aim*value

print(f"PART B: the product of coordinates under the new scheme is {horiz*depth}")
