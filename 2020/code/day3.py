import pandas as pd
import numpy as np

data_file = "../data/day3.txt"
data = pd.read_table(data_file, names=['field'])

def get_trees(field, right, down):

	# expand field to what we'll need
	nrows = len(field.index)
	ncols = len(field['field'][0])
	
	# find what symbol is at the important place
	field['symbol_at_pos'] = '0'
	for i in range(0, len(field.index), down):
		
		# get string index with pbc (thanks, mayk)
		str_index = right/down*i
		str_index_wrapped = int(str_index % ncols)
		
		# get symbol		
		field['symbol_at_pos'][i] = field['field'][i][str_index_wrapped]

	# how many trees are there
	return np.sum(field['symbol_at_pos'] == '#')

# part 1 
print(f"part 1: the number of trees is {get_trees(data, right=3, down=1)}")

# part 2
prod = get_trees(data, right=1, down=1) * \
		get_trees(data, right=3, down=1) * \
		get_trees(data, right=5, down=1) * \
		get_trees(data, right=7, down=1) * \
		get_trees(data, right=1, down=2)
		
print(f"the product of the trees we care about is {prod}")
