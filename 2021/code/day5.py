# data
data_file = "../data/day5.txt"

# read in data and split it into number draws and boards
import re
import numpy as np

data = open(data_file, 'r').read().split('\n')
data = np.array([[int(n) for n in re.split(',| -> ', line)] for line in data])

# function to track/count number of vent points given data slopes
def count(data, slopes, no_diags=True): 
    field_size = np.max(data) + 1
    field = np.zeros([field_size, field_size])
    for i,row in enumerate(data):

        m = slopes[i]

        if no_diags:    
            if (np.isfinite(m)) and (abs(m) > 0):
                # this is not a vertical or horizontal line
                continue

        if np.isfinite(m):
            # regular line case
            i0 = row[0]
            j0 = row[1]
            i_last = row[2]
            order = 1 if i_last > i0 else -1

            for i in range(i0, i_last+order, order):
                if int(m*(i-i0)) == m*(i-i0):
                    field[j0+int(m*(i-i0)),i] += 1
        
        else:
            # vertical line case
            i0 = row[0]
            j0 = row[1]
            j_last = row[3]
            order = 1 if j_last > j0 else -1

            for j in range(j0, j_last+order, order):
                field[j,i0] += 1

    n_pts = np.sum(field > 1)

    return n_pts


# get slope column (not adding to data because makes everything a float)
with np.errstate(divide='ignore'):
    slopes = (data[:,3] - data[:,1] ) / (data[:,2] - data[:,0])

# PART A: for vertical and horiz lines, how many points are crossed more than once?
n_pts_nodiags = count(data,slopes,no_diags=True)
print(f"PART A: there are {n_pts_nodiags} points where there is more than one vent")

# PART B: for all lines, how many points are crossed more than once?
n_pts_diags = count(data,slopes,no_diags=False)
print(f"PART B: there are {n_pts_diags} points where there is more than one vent")