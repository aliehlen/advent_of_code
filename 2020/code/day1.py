data_file = "../data/day1.txt"

# get data
data = open(data_file).readlines()
data = [int(d) for d in data]

# part 1 - product of the 2 values sum to 2020

for i in range(len(data)):
    n1 = data[i]
    for n2 in data[i:]:   
        nsum = n1 + n2
        if nsum == 2020:
            print(f"the numbers are {n1} and {n2}")
            print(f"their product is {n1*n2}")
            break

# part 2 - product of the 3 values sum to 2020

for i in range(len(data)):
    n1 = data[i]
    for j in range(len(data[i:])):  
        n2 = data[i+j] 
        for n3 in data[i+j:]:
            nsum = n1 + n2 + n3
            if nsum == 2020:
                print(f"the numbers are {n1}, {n2}, and {n3}")
                print(f"their product is {n1*n2*n3}")
                break