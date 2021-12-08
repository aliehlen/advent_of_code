# data
data_file = "../data/day7.txt"

# read in data and split it into number draws and boards
import numpy as np
data = np.array(list(map(int,open(data_file, 'r').read().split(','))))

# PART A: calculate the costs as a sum
cur_min = 100000000
cur_i = 0

for i in range(0,max(data)+1):
    new_min = min(cur_min, sum(np.abs(data - i)))

    if (new_min < cur_min):
        cur_min = new_min
        cur_i = i

print(f"PART A: the lowest cost is {cur_min} at position {cur_i}")

# PART B: caculate the costs differently

# precalculate the sums
max_dist = np.max(data)
all_costs = np.zeros(max_dist+1)

for i in range(1,max_dist+1):
    all_costs[i] = all_costs[i-1]+i

# now find min cost
cur_min = 100000000
cur_i = 0

for i in range(0,max(data)+1):
    dists = np.abs(data - i)
    cursum = sum(all_costs[dists])

    new_min = min(cur_min, cursum)

    if (new_min < cur_min):
        cur_min = new_min
        cur_i = i

print(f"PART B: the new lowest cost is {cur_min} at position {cur_i}")
