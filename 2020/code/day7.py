import re
import numpy as np

def read_in_rules(rules):
	""" read, clean rules into dict"""
	
	rules = [re.sub("bags|bag|\.", "", s) for s in rules]
	
	bag_dict = {s.split("contain")[0].strip(): s.split("contain")[1].strip() for s in rules}

	bag_map = {}
	for bag, subbags in bag_dict.items():
		bag_map[bag]= {}
		for subbag in subbags.split(","):
			try:
				bag_map[bag][re.sub('\d', '', subbag).strip()] = int(re.findall('\d', subbag)[0])
			except IndexError:
				bag_map[bag][subbag] = 0
				
	return(bag_map)


def get_parent_bags(rules, child_bags):
	pass


data_file = "../data/day7.txt"
data = open(data_file, 'r').read().split("\n")

# clean
bag_rules = read_in_rules(data)

# part 1

bags = ['shiny gold']

still_looking = True
parents = []
next_parents = []

while still_looking:

	for this_bag in bags:	
		for bag, subbag in bag_rules.items():
			if this_bag in subbag:
				parents.append(bag)
				next_parents.append(bag)
	
	bags = next_parents
	next_parents = []
	
	if len(bags) == 0:
		still_looking = False

num_parents = len(np.unique(parents))	

print(f"part 1: the number of possible outer bags is {num_parents}")

# part 2 

def get_num_bags(bag):
	
	if bag == 'no other':
		return 0
	
	else:
		in_bag = bag_rules[bag]
		num_bags = sum([in_bag[b]*(1+get_num_bags(b)) for b in in_bag])
		return num_bags
	
print(f"part 2: a shiny gold bag holds {get_num_bags('shiny gold')}")