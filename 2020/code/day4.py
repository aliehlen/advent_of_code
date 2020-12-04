import pandas as pd
import numpy as np

def yr_in_range(col, min_yr, max_yr):
	""" return boolean mask: each entry 4 numbers between min_yr and max_yr """
	col_mask = col.str.match('[0-9]{4}') == True
	col_int = col.astype(int)
	col_mask = col_mask & (col_int >= min_yr) & (col_int <= max_yr)
	return col_mask


def height_in_range(col, unit, ht_min, ht_max):
	""" return boolean mask: each entry in right units and btwn ht_min and ht_max """
	right_unit = col.str.match("[0-9]+["+unit+"]") == True
	height_int = col.str.extract('(^[0-9]+)').astype(int)[0]
	col_mask = right_unit & (height_int >= ht_min) & (height_int <= ht_max)
	return col_mask
	

data_file = "../data/day4.txt"
file = open(data_file, 'r')
all_text = file.read()

# process the text
all_docs = all_text.split("\n\n")

# what fields do we care about
required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
not_needed = 'cid'

# prep df of fields 
all_rows = []
for doc in all_docs:
	doc_pts = doc.split()
	all_rows.append({field.split(":")[0]:field.split(":")[1] for field in doc_pts})
	
df = pd.DataFrame(all_rows)
del df['cid']

# part 1 - how many ppts have all non cid fields?

df = df[~df.isna().any(axis=1)]
print(f"part 1: there are {len(df.index)} valid docs")

# part 2 - add more stringent requirements

# collect masks we need

# hcl
m1 = df['hcl'].str.match('#[a-f|0-9]{6}') == True

# pid
m2 = df['pid'].str.match('^[0-9]{9}$') == True

# ecl
eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
m3 = df['ecl'].isin(eye_colors)

# byr
m4 = yr_in_range(df['byr'], 1920, 2002)

# iyr
m5 = yr_in_range(df['iyr'], 2010, 2020)

# eyr
m6 = yr_in_range(df['eyr'], 2020, 2030)

# hgt
m7 = height_in_range(df['hgt'], 'cm', 150, 193) | \
		height_in_range(df['hgt'], 'in', 59, 76)

# put all the masks together
df_valid = df[m1 & m2 & m3 & m4 & m5 & m6 & m7]

print(f"part 2: there are {len(df_valid.index)} valid docs")
