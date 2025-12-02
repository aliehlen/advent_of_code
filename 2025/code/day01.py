with open('../data/day01.dat') as f:
    lines = f.readlines()

# first star

max_value = 100
position = 50

position_list = []

for line in lines:
    
    direction = 1 if line[0] == "R" else -1
    magnitude = int(line[1:].rstrip())

    position = (position + direction*magnitude) % max_value
    position_list.append(position)

n_zeros = len([p for p in position_list if p == 0])

print(f"* the dial points at zero {n_zeros} times")

# second star

max_value = 100
position = 50

n_zeros = 0

for line in lines:
    
    direction = 1 if line[0] == "R" else -1
    magnitude = int(line[1:].rstrip())

    dist_to_zero = max_value - position if direction == 1 else position

    if position == 0:
        dist_to_zero = max_value

    if magnitude >= dist_to_zero:
        n_zeros += 1
        n_zeros += (magnitude - dist_to_zero) // max_value

    position = (position + direction*magnitude) % max_value

print(f"** the dial passes zero {n_zeros} times")