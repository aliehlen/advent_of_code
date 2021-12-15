# data
data_file = "../data/day14.txt"

import collections
import itertools

data = open(data_file, 'r').read().split('\n\n')

template = data[0]

rules = [line.split(" -> ") for line in data[1].split("\n")]

rules_pA = {rule[0]:rule[1]+rule[0][1] for rule in rules}

# PART A: apply rules 10 times
def polymerize(template, n):
    polymer = template
    for i in range(0,n):
        lngth = len(polymer)-1
        polymer = polymer[0] + ''.join([rules_pA[polymer[i:i+2]] for i in range(0,lngth)])

    return polymer
    
polymer = polymerize(template, 10)
print("counting...")
n_each = collections.Counter(polymer).values()
print(f"PART A: the difference between the max and min occurances is {max(n_each) - min(n_each)}")


# PART B: apply rules for 40 steps
# too slow to do it like part A

# rules: which pairs are created from each pair (i.e. NA -> B becomes NA: [NB, BA])
rules_pB = {rule[0]:[rule[0][0]+rule[1],rule[1]+rule[0][1]] for rule in rules}

# make template into dicionary that tracks how many of each pair exist
all_pairs = {pair:0 for pair in rules_pA}
for i in range(0,len(template)-1):
    all_pairs[template[i:i+2]] += 1

# run through all 40 steps of polymerization even though I don't think this is how polymerization works
n_part2 = 40
for i in range(0,n_part2):

    # we need to get info from and modify the dict at the same time
    current_pairs = all_pairs.copy()
    
    for pair in all_pairs:

        pairs_created = rules_pB[pair]

        # we've destroyed all instances of this pair and created two others
        all_pairs[pair] -= current_pairs[pair]
        all_pairs[pairs_created[0]] += current_pairs[pair]
        all_pairs[pairs_created[1]] += current_pairs[pair]

# count number of each node based on the number of each pair
all_nodes = {n:0 for n in set([rule[1] for rule in rules])}

for pair, num_pair in all_pairs.items():
    all_nodes[pair[0]] += num_pair
    all_nodes[pair[1]] += num_pair

# everyone will be double counted except the first and last, 
# so need to compensate for htat)
all_nodes[template[0]] += 1
all_nodes[template[-1]] += 1

max_val = max(all_nodes.values())/2
min_val = min(all_nodes.values())/2

print(f"PART B: the difference between the max and min occurances after 40 steps is {int(max_val - min_val)}")
