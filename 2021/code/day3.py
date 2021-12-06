# data
data_file = "../data/day3.txt"


def get_decimal(binary):
    return sum(v*2**(len(binary) - 1 - i) for i,v in enumerate(binary))


# read in matrix of integers
import numpy as np

data = np.genfromtxt(data_file, dtype=str)
data = np.array([[int(d) for d in line] for line in data])

# PART A
# get rates
n_pts = data.shape[0]
sum_of_cols = np.sum(data, axis=0)

# gamma rate = most common number, epsilon rate = least common
gamma_rate = [1 if n > n_pts/2 else 0 for n in sum_of_cols]
epsilon_rate = [0 if n > n_pts/2 else 1 for n in sum_of_cols]

power_consumption = get_decimal(gamma_rate) * get_decimal(epsilon_rate)

print(f"PART A: power consumption is {power_consumption}")

# PART B
# filter matrix based on criteria
def filter(criteria, matrix, col):
    n_pts = matrix.shape[0]

    if criteria == "oxygen":
        keep = 1 if sum(matrix[:,col]) >= n_pts/2 else 0
    elif criteria == "CO2":
        keep = 0 if sum(matrix[:,col]) >= n_pts/2 else 1
    
    return matrix[matrix[:,col] == keep,:]


# get oxygen generator rating
filtered_data = data

for i in range(data.shape[1]):
    filtered_data = filter("oxygen", filtered_data, i)
    if filtered_data.shape[0] == 1:
        oxygen_rating = filtered_data[0]
        break

# get CO2 scrubber rating
filtered_data = data

for i in range(data.shape[1]):
    filtered_data = filter("CO2", filtered_data, i)
    if filtered_data.shape[0] == 1:
        co2_rating = filtered_data[0]
        break

# put them all together
life_support = get_decimal(oxygen_rating) * get_decimal(co2_rating)

print(f"PART B: life support rating is {life_support}")  