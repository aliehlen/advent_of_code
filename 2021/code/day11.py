# data
data_file = "../data/day11.txt"

# read in data and split it into number draws and boards
import numpy as np
data = np.genfromtxt(data_file, delimiter=1)

# PART A: how many flashes after 100 steps?
# data = np.pad(data, 1) 
field_size = 10

# create a ring of 1 around the coordinate 0,0 . pad to deal with pbc
flash = np.zeros((field_size+2,field_size+2))
pts_arround_00 = np.array([[1,2], [2,2], [2,1], [2,0], [1,0], [0,0], [0,1], [0,2]])
flash[tuple(pts_arround_00.T)] = 1

# track total number of flashes per step, number new 
number_of_flashes = 0
number_new_flashes = 0
step = 0

# one step
while step <= 100 or number_new_flashes != data.size:

    # add one and figure out which octopuses are flashing now
    data += 1
    all_flashes = np.array(np.where(data > 9)).T
    new_flashes = all_flashes

    while len(new_flashes) > 0:

        # add the flash mask to any that flashed this time (make sure to remove padding)
        for flash_pt in new_flashes:
            data += np.roll(flash, flash_pt, (0,1))[1:11,1:11]

        # get list of the one octoposes that flashed
        new_all_flashes = np.array(np.where(data > 9)).T

        new_flashes = np.array([p for p in new_all_flashes if not (all_flashes == p).all(1).any()])
        all_flashes = new_all_flashes


    # reset the ones that flashed back to zero
    number_new_flashes = len(data[data > 9])
    number_of_flashes += number_new_flashes
    data[data > 9] = 0
    step += 1

    if step == 100:
        print(f"PART A: there have been {number_of_flashes} flashes after 100 steps")

    if number_new_flashes == data.size:
        print(f"PART B: All the octopuses flashed! It's step {step}")



