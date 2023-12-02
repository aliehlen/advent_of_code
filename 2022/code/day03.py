# data
data_file = "../data/day03.dat"

# read data
import string

priorities = string.ascii_lowercase + string.ascii_uppercase

data = [[l[:len(l)//2], l[len(l)//2:]] for l in open(data_file, 'r').read().split("\n")]

# part 1

common = [list(set(c[0]).intersection(c[1]))[0] for c in data]
score = sum([priorities.index(s)+1 for s in common])

print(f"the total priority is {score}")

# part 2

data = [l for l in open(data_file, 'r').read().split("\n")]

common_score = 0
for elf_i in range(0,len(data),3):
    common = set(data[elf_i]).intersection(data[elf_i + 1]).intersection(data[elf_i + 2])
    common = list(common)[0]

    common_score += priorities.index(common) + 1

print(f"the total priority of the badges is {common_score}")
