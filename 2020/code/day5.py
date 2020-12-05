import pandas as pd
import numpy as np

def search_tree(directions, tree, left, right):
	if len(directions) == 1:
		return(tree[0] if directions[0] == left else tree[1])
	else:
		if directions[0] == left:
			return(search_tree(directions[1:], tree[:len(tree)//2], left, right))
		elif directions[0] == right:
			return(search_tree(directions[1:], tree[len(tree)//2:], left, right))


row_depth = 7
col_depth = 3

data_file = "../data/day5.txt"
data = pd.read_csv(data_file, names=['seat_all'])

# format data so have row and column info separately
data['seat_row'] = data['seat_all'].str[0:row_depth]
data['seat_column'] = data['seat_all'].str[row_depth:row_depth+col_depth]

# add in row and column number
all_rows = list(range(0,2**row_depth))
data['row_num'] = [search_tree(dir, all_rows, 'F', 'B') \
					for dir in data['seat_row']]
					
all_cols = list(range(0,2**col_depth))
data['col_num'] = [search_tree(dir, all_cols, 'L', 'R') \
					for dir in data['seat_column']]

# add in seat id
data['seat_id'] = data['row_num']*8 + data['col_num']

# part 1 - highest seat id

print(f"part 1: the highest seat id is {data['seat_id'].max()}")

# part two - which seat is missing (for which surrounding seats also exist)

all_possible_seats = set(range(data['seat_id'].min(), data['seat_id'].max()+1))
missing_seat = all_possible_seats.difference(data['seat_id'])

print(f"part 2: the missing seat id is {missing_seat}")
