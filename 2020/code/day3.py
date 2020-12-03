import pandas as pd
import numpy as np

data_file = "../data/day3.txt"
data = pd.read_table(data_file, names=['field'])

def get_trees(field, right, down):

	# expand field to what we'll need
	nrows = len(field.index)
	ncols = len(field['field'][0])

	cols_needed = np.ceil((right/down)*nrows) 
	copies_needed = int(np.ceil(cols_needed / ncols)) 

	field['field_expanded'] = [row*copies_needed for row in field['field']]
	
	# find what symbol is at the important place
	field['symbol_at_pos'] = '0'
	for i in range(0, len(field.index), down):
		
		# only count if have integer index
		str_index = right/down*i
		if np.floor(str_index) != str_index:
			continue
		
		# get symbol		
		field['symbol_at_pos'][i] = field['field_expanded'][i][int(str_index)]

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