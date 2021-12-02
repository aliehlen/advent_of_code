import numpy as np

def get_neighbors(row, col, data):
	
	rmin = 0 if row == 0 else -1
	rmax = 0 if row == data.shape[0]-1 else 1
	cmin = 0 if col == 0 else -1
	cmax = 0 if col == data.shape[1]-1 else 1
	
	rrange = range(rmin, rmax+1)
	crange = range(cmin, cmax+1)
	
	n = [data[row+r,col+c] for r in rrange for c in crange if not r == c == 0]
	
	return(n)
	

# main

data_file = "../data/day11.txt"
data = np.array([list(s) for s in open(data_file, 'r').read().split("\n")])


# part 1 - pretty inefficient

next = np.copy(data)
done = False
		
		
		
while not done:
	
	data = np.copy(next)
	
	for i, row in enumerate(data):
		for j, val in enumerate(row):
		
			if val == ".":
				continue
			
			neighbors = get_neighbors(i, j, data)
			
			if val == "L":
				if not any([ n == '#' for n in neighbors ]):
					next[i, j] = '#'
					
			elif val == "#": 
				if sum([n == '#' for n in neighbors]) >= 4:
					next[i, j] = 'L'

	if (next == data).all():
		done = True

print(f"part 1: number of occupied seats is {np.sum(data == '#')}")
	
# part 1 
# try with numpy (making occupied seats 1, shifting by +-1, adding up, changing 
# seats where is L or # and meets criteria
	
# part 2
