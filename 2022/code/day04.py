# data
data_file = "../data/day04.dat"

# read data
import numpy as np
import re

data = np.array([[int(n) for n in re.split(",|-", l)] for l in open(data_file, 'r').read().split("\n")])

# part 1
contains = np.sum((data[:,0] <= data[:,2]) & (data[:,1] >= data[:,3]) |
                  (data[:,2] <= data[:,0]) & (data[:,3] >= data[:,1]))

print(f"the total number of rows where one contains the other is {contains}")

# part 2
overlap = np.sum((data[:,0] <= data[:,2]) & (data[:,1] >= data[:,2]) |
                 (data[:,0] <= data[:,3]) & (data[:,1] >= data[:,3]) |
                 (data[:,2] <= data[:,0]) & (data[:,3] >= data[:,0]) | 
                 (data[:,2] <= data[:,1]) & (data[:,3] >= data[:,1])) 

total_overlap = overlap

print(f"the total number of rows where one overlaps the other is {total_overlap}")
