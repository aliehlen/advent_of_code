# data
data_file = "../data/sample.txt"

import numpy as np

# data
data = np.genfromtxt(data_file, delimiter=1)

# PART A: lowest risk (from 0,0)

# risks is matrix of the min path to 0,0 from each point in the field
risk_matrix = np.zeros_like(data)

def get_risk(i_val, j_val, risks):

    if i_val == 0 and j_val == 0:
        return 0

    elif risks[j_val, i_val] != 0:
        return risks[j_val, i_val] 

    elif risks[j_val, i_val] == 0:

        new_matrix = risks.copy()
        new_matrix[j_val, i_val] = 100000000
        
        l = get_risk(i_val-1,j_val,new_matrix) if i_val > 0 else 100000000
        r = get_risk(i_val+1,j_val,new_matrix) if i_val < risks.shape[1]-1 else 100000000
        t = get_risk(i_val,j_val-1,new_matrix) if j_val > 0 else 100000000
        b = get_risk(i_val,j_val+1,new_matrix) if j_val < risks.shape[0]-1 else 100000000
    
        return data[j_val, i_val] + min(l, r, t, b)

for i in range(0,risk_matrix.shape[0]):
    for j in range(0,risk_matrix.shape[1]):
        print(risk_matrix)
        risk_matrix[j,i] = get_risk(i,j,risk_matrix)

print(risk_matrix)

print(f"PART A: the total risks to get to the lower right corner is {int(risk_matrix[-1,-1])}")