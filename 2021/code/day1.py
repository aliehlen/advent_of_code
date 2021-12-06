# data
data_file = "../data/day1.txt"

# read in list of integers
data = list(map(int, open(data_file, 'r').read().split("\n")))

# PART A
# find number of steps for which depth is increasing
num_increase = sum(i < j for i,j in zip(data[:-1], data[1:]))

print(f"PART A: there are {num_increase} depth increases.")

# PART B
# find number of increases in a sliding 3-number sum
data_w = [sum(data[i:i+3]) for i in range(len(data)-2)]
num_w_increase = sum(i < j for i,j in zip(data_w[:-1], data_w[1:]))

print(f"PART B: there are {num_w_increase} depth window increases.")
