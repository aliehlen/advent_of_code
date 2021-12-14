# data
data_file = "../data/day13.txt"

data = open(data_file, 'r').read().split('\n\n')
import numpy as np

points = np.array([[int(n) for n in line.split(",")] for line in data[0].split("\n")])
instructions = [line.replace("fold along ","").split("=") for line in data[1].split("\n")]

# PART A: do first fold
command = instructions[0]
axis = command[0]
fold_loc = int(command[1])
if axis == 'x':
    points[:,0] = np.where(points[:,0] > fold_loc, 2*fold_loc - points[:,0], points[:,0])

elif axis == "y":
    points[:,1] = np.where(points[:,1] > fold_loc, 2*fold_loc - points[:,1], points[:,1])


print(f"PART A: there are {len(np.unique(points, axis=0))} points visible after the first fold")

# PART B: what letters do we see after the fold?

# same code, now just in a loop
for command in instructions:
    axis = command[0]
    fold_loc = int(command[1])
    if axis == 'x':
        points[:,0] = np.where(points[:,0] > fold_loc, 2*fold_loc - points[:,0], points[:,0])
        
    elif axis == "y":
        points[:,1] = np.where(points[:,1] > fold_loc, 2*fold_loc - points[:,1], points[:,1])

    points = np.unique(points, axis=0)

# print field nicely
field_size = np.max(points)
field = np.full(shape=(field_size+1,field_size+1), fill_value=".")
field[tuple(points.T)] = "#"

np.savetxt("../misc/day13.dat", field.T, delimiter="", fmt='%s')
