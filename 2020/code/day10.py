import numpy as np
from collections import Counter


data_file = "../data/day10.txt"
data = np.fromfile(data_file, sep="\n")

# part 1 - distribution of diffs

data = np.sort(data)

diffs = np.diff(data, prepend = 0, append = data[-1]+3)
diffs_counts = Counter(diffs)

print(f"part 1: 1 jolt diffs x 3 jolt diffs: {diffs_counts[1]*diffs_counts[3]}")

# part 2 - num arrangements

# how many are removable independently?
remables = np.array([diffs[i] if (diffs[i]==diffs[i+1]==1) else 0 for i in range(len(diffs[0:-1])) ], dtype=int)

# can't remove 3 or more in a row, so need to know how many 3+ runs of 1s 
# this only works if there are no runs of more than 3
lens = [len(s) for s in ''.join(remables.astype(str)).split('0')]
num_3s = Counter(lens)[3]

# number of configs with at least one run of 3 - use numpy to fit bigger numbers

all_configs = np.array(2, dtype=np.float64)**sum(remables)
other_configs = np.array(2**(sum(remables)-3*num_3s), dtype=np.float64)
run_configs = np.array((1+(2**3-1))**num_3s - (2**3-1)**num_3s, dtype=np.float64)

all_configs = 2.0**sum(remables)
other_configs = 2.0**(sum(remables)-3*num_3s)
run_configs = (1.0+(2**3-1))**num_3s - (2**3-1)**num_3s



print(f"part 2: the number of possible configurations is {all_configs - other_configs*run_configs}")


# the math to calc num_3_runs
# [all configs of all other spaces]*[ configs of all runs where at least one run of 3 are all removed ]
# [2^(all_removable - removables_in_runs)]*[ (1 + (2^3 -1))^num_runs - (2^3 -1)^num_runs] <- last one removes case where no runs are all removed

# num_3_runs = 2**(sum(remables)-3*num_3s) * ( (1+(2**3-1))**num_3s - (2**3-1)**num_3s )

