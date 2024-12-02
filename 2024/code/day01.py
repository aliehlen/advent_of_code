with open('../data/day01.dat') as f:
    lines = f.readlines()

# ----- phase 1: compare lists -----

# parse numbers
list1 = []
list2 = []

dists = []

for line in lines:
    col1,col2 = [int(num) for num in line.split()]

    list1.append(col1)
    list2.append(col2)

# sort lists
list1.sort()
list2.sort()

# get dists
dists = [abs(int(col1) - int(col2)) for col1,col2 in zip(list1,list2)]
total_dists = sum(dists)

# report out
print(f"phase 1: the sum of distances is {total_dists}")

# ----- phase 2: similarity score -----

import collections

occurances_list2 = collections.Counter(list2)

similarity_score = 0
for number in list1:
    similarity_score += number*occurances_list2[number]

# report out
print(f"phase 2: the similarity score is {similarity_score}")

