# data
data_file = "../data/day9.txt"

# read in data and split it into number draws and boards
import numpy as np

data = np.genfromtxt(data_file, delimiter=1)

# PART A: find all low points

def find_lowest(data):

    extracol = np.array([[9]]*data.shape[0])
    extrarow = np.array([[9]*data.shape[1]])

    # for each point, subtract neighbor to left, right, up, down
    left = data - np.concatenate((extracol, data[:,:-1]), axis = 1)
    right = data - np.concatenate((data[:,1:], extracol), axis = 1)

    up = data - np.concatenate((extrarow, data[:-1,:]), axis = 0)
    down = data - np.concatenate((data[1:,:], extrarow), axis = 0)

    # return mask of which are lowest
    lowest = (left < 0) & (right < 0) & (up < 0) & (down < 0)

    return lowest

lowest_pt_coords = find_lowest(data)

print(f"PART A: the total danger score {sum(data[lowest_pt_coords] + 1)}")

# PART B: size of largest basins

# mark all the basins with 1s
all_basins = (data < 9)*1
all_basins_padded = np.pad(all_basins, 1)

# get size of basin that contains (x,y) 
def get_basin_size(x,y):
    if all_basins_padded[x,y] == 0:
        return 0
    elif all_basins_padded[x,y] == 1:
        all_basins_padded[x,y] = 0
        return 1 + get_basin_size(x-1,y) + \
                    get_basin_size(x+1,y) + \
                    get_basin_size(x,y-1) + \
                    get_basin_size(x,y+1)

# get list of x, y indices of the lowest points from part A
x,y = np.nonzero(lowest_pt_coords)

# find the size of the basin corresponding to each point
basin_sizes = []
for i,j in zip(x+1,y+1): # add one because of padding 
    basin_sizes.append(get_basin_size(i,j))

basin_sizes.sort(reverse=True)

print(f"PART B: the product of the size of the 3 largest basins is {np.product(basin_sizes[0:3])}")
