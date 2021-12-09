# data
data_file = "../data/day9.txt"

# read in data and split it into number draws and boards
import numpy as np

data = np.genfromtxt(data_file, delimiter=1)
# data = np.pad(data, 1, constant_values=9)

def find_lowest(data, row, col):

    # for each point, subtract neighbor to left, right, up, down
    left = data - np.concatenate((col, data[:,:-1]), axis = 1)
    right = data - np.concatenate((data[:,1:], col), axis = 1)

    up = data - np.concatenate((row, data[:-1,:]), axis = 0)
    down = data - np.concatenate((data[1:,:], row), axis = 0)

    # return mask of which are lowest
    lowest = (left < 0) & (right < 0) & (up < 0) & (down < 0)

    return lowest

# PART A: find all low points
extracol = np.array([[9]]*data.shape[0])
extrarow = np.array([[9]*data.shape[1]])

lowest_pt_coords = find_lowest(data, extrarow, extracol)

print(f"PART A: the total danger score {sum(data[lowest_pt_coords] + 1)}")

# PART B: size of largest basins
all_basins = (data < 9)*1

# get list of x, y indices of the lowest points from part A
x,y = np.nonzero(lowest_pt_coords)

# pad with zeros to prep for analysis
cur_field = np.pad(all_basins, 1)

# get size of basin that contains (x,y) 
def get_basin_size(x,y):
    if cur_field[x,y] == 0:
        return 0
    elif cur_field[x,y] == 1:
        cur_field[x,y] = 0
        return 1 + get_basin_size(x-1,y) + \
                    get_basin_size(x+1,y) + \
                    get_basin_size(x,y-1) + \
                    get_basin_size(x,y+1)

# find the size of the basin corresponding to each point
basin_sizes = []
for i,j in zip(x+1,y+1): # add one because of padding 
    basin_sizes.append(get_basin_size(i,j))

basin_sizes.sort(reverse=True)

print(f"PART B: the product of the size of the 3 largest basins is {np.product(basin_sizes[0:3])}")



# def get_basin_size(x,y,dat):
#     if dat[x,y] == 0:
#         return 0
#     elif dat[x,y] == 1:
#         dat[x,y] = 0
#         return 1 + get_basin_size(x-1,y,dat) + \
#                     get_basin_size(x+1,y,dat) + \
#                     get_basin_size(x,y-1,dat) + \
#                     get_basin_size(x,y+1,dat)

# this could fail if there are points next to each other of the same height
# cur_data = np.copy(data)
# all_basins = np.zeros_like(data)
# new_basins = all_basins + 1

# while np.sum(new_basins) > 0:
#     new_basins = find_lowest(cur_data, extrarow, extracol)
#     all_basins += new_basins
#     cur_data[new_basins] = 9