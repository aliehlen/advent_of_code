# data
data_file = "../data/day01.dat"

# read data
data = [[int(n) for n in l.split("\n")] for l in open(data_file, 'r').read().split("\n\n")]

# star 1: how many calories is the elf with the most calories carrying?
max_elf = max([sum(cals) for cals in data])

print(f"the max calories carried by an elf is {max_elf}")

# star 2: how many calories are the top three elves carrying?
all_elves = [sum(cals) for cals in data]
all_elves.sort(reverse=True)

max_three_elves = sum(all_elves[0:3])

print(f"the calories carried by the top three elves is {max_three_elves}")
