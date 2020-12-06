from collections import Counter

data_file = "../data/day6.txt"
data = open(data_file, 'r').read().split("\n\n")

# part 1 - number of letters which appear in at least one line per group

# remove extra spaces
total_counts = sum([len(set(s.replace("\n", "" ))) for s in data])

print(f"part 1: sum of unique answers is {total_counts}")

# part 2 - number of letters which appear in every line per group

# now extra newlines matter. keep those
data2 = [s.split() for s in data]

# count instances per group where the number of times a letter appears is equal 
# to the number of lines in the group
cnts = [sum([len(s) == c for c in Counter(''.join(s)).values()]) for s in data2]

print(f"part 2: sum of unique answers is {sum(cnts)}")


