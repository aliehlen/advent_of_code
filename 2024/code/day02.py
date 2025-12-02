with open('../data/test.dat') as f:
    lines = f.readlines()

lines = [[int(num) for num in line.split()] for line in lines]

# ----- part 1 -----

safe = len(lines)

for line in lines:
    diff = [n2-n1 for n1,n2 in zip(line[0:-1], line[1::])]
    
    positive = (diff[0] >= 0)
    for d in diff:
        
        if (positive != (d >= 0)) or (abs(d) < 1 or abs(d) > 3):
            safe -= 1
            break

print(f"there are {safe} safe reports in the data")

# ----- part 2 -----

safe = len(lines)

for line in lines:
    print(line)
    diff = [n2-n1 for n1,n2 in zip(line[0:-1], line[1::])]
    print(diff)
    
    positive = (diff[0] >= 0)
    issues = 0

    for d in diff:
        
        if (positive != (d >= 0)) or (abs(d) < 1 or abs(d) > 3):
            issues += 1
            break
        
        if issues >= 2:
            safe -= 1
            break
    print(issues)

print(f"there are {safe} safe reports in the data")