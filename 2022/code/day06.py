# data
data_file = "../data/day06.dat"

# prep
import collections

# read data
data = [line for line in open(data_file, 'r').read().split("\n")][0]

# part 1
current_letters = [' '] + [*data[0:3]]

for i,letter in enumerate(data):
    
    if i < 3:
        continue

    current_letters.pop(0)
    current_letters.append(letter)

    if max(collections.Counter(current_letters).values()) == 1:
        end_of_marker = i+1
        break

print(f"the end of marker location is {end_of_marker}")

# part 2
current_letters = [' '] + [*data[0:13]]

for i,letter in enumerate(data):
    
    if i < 13:
        continue

    current_letters.pop(0)
    current_letters.append(letter)

    if max(collections.Counter(current_letters).values()) == 1:
        message = i+1
        break

print(f"the message location is {message}")

