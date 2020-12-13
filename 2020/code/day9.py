from itertools import combinations as comb

data_file = "../data/day9.txt"
data = open(data_file, 'r').read().split("\n")
data = [int(s) for s in data]

# part 1

window = 25

invalids = [data[i] for i in range(window, len(data)) if not any([sum(c)==data[i] for c in comb(data[i-window:i], 2)])]

print(f"part 1: the first invalid value is {invalids[0]}")

# part 2

target = invalids[0]

for i in range(len(data)):
	s = 0
	j = i
	while s < target:
		s += data[j]
		j += 1
	if s == target:
		break
		
min_val = min(data[i:j+1])
max_val = max(data[i:j+1])	

print(f"part 2: the sum of min, max in range is {min_val + max_val}")
