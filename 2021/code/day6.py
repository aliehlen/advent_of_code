# data
data_file = "../data/day6.txt"

# read in data and split it into number draws and boards
import numpy as np
data = list(map(int,open(data_file, 'r').read().split(',')))

# don't track each fish - track how many have a given number of days left
lanternfish = np.array([0]*9)
for i in data:
    lanternfish[i] +=1

# PART A: grow laternfish for 80 days
for day in range(80):
    lanternfish = np.roll(lanternfish, -1)
    lanternfish[6] += lanternfish[8]

print(f"PART A: there are {sum(lanternfish)} after 80 days")

# PART B: grow laternfish for 256 days - reset lanternfish first
lanternfish = np.array([0]*9,dtype='int64')
for i in data:
    lanternfish[i] +=1

for day in range(256):
    lanternfish = np.roll(lanternfish, -1)
    lanternfish[6] += lanternfish[8]

print(f"PART B: there are {sum(lanternfish)} after 80 days")
