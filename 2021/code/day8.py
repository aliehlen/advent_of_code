# data
data_file = "../data/day8.txt"

# read in data and split it into number draws and boards
import numpy as np

data = open(data_file, 'r').read().split('\n')

# PART A: get number of outputs with specific lens
lens = np.array([[len(s) for s in line.partition(" | ")[2].split()] for line in data])

lens_of_interest = [2,3,4,7]
all_lens = sum(np.sum(lens == i) for i in lens_of_interest)

print(f"PART A: the number of 1, 4, 7, 8 output is: {all_lens}")

# PART B: decode the outputs
import sys
# reparse the data in a way that's more useful
inputs = np.array([[set(s) for s in line.partition(" | ")[0].split()] for line in data])
outputs = np.array([[set(s) for s in line.partition(" | ")[2].split()] for line in data])

# make a list of digits for each row
decode = []
for i,row in enumerate(inputs):
    new_row = [''] * 10
    
    # 1, 4, 7, 8 are already determined
    new_row[1] = next(s for s in row if len(s) == 2)
    new_row[4] = next(s for s in row if len(s) == 4)
    new_row[7] = next(s for s in row if len(s) == 3)
    new_row[8] = next(s for s in row if len(s) == 7)

    # get those of length 6
    new_row[9] = next(s for s in row if len(s) == 6 and new_row[4].issubset(s))
    new_row[0] = next(s for s in row if len(s) == 6 and new_row[1].issubset(s) and s not in new_row)
    new_row[6] = next(s for s in row if len(s) == 6 and s not in new_row)

    # get those of length 5
    new_row[3] = next(s for s in row if len(s) == 5 and new_row[7].issubset(s))
    new_row[5] = next(s for s in row if len(s) == 5 and s.issubset(new_row[6]))
    new_row[2] = next(s for s in row if len(s) == 5 and s not in new_row)

    # add output (converting to actual integers)
    digits = [new_row.index(set(n)) for n in outputs[i]]
    decode.append(sum([d*10**(len(digits)-1 - j) for j,d in enumerate(digits)]))

# calculate actual numbers and add them up
print(f"PART B: the sum of the decoded outputs is {sum(decode)}")


