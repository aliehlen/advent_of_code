# data
data_file = "../data/day12.txt"

data = open(data_file, 'r').read().split('\n')
data = [ line.split("-") for line in data ]

# reconfigure the data a little
all_nodes = list(set([n for pth in data for n in pth])) #  if n not in ['start', 'end']

# build adjacency list (dict with one entry per node, which is a list ofits children)
adjacency_list = {n:[] for n in all_nodes} 
for pair in data:
    if pair[1] != "start": adjacency_list[pair[0]].append(pair[1])
    if pair[0] != "start": adjacency_list[pair[1]].append(pair[0])


# PART A: get the path from any node to the end recursively 
def get_path_to_end(n, adj_list):

    if n == "end":
        return [['end']]

    else:
        children_of_n = adj_list[n]

        if n.islower():
            # can't come back here, remove n from the adjacency list
            adj_list = {k:[ch for ch in v if ch != n] for k,v in adj_list.items() if k != n}

        child_paths = [path for child in children_of_n for path in get_path_to_end(child, adj_list)]

        return [[n, *path] for path in child_paths]


paths_to_end = get_path_to_end('start', adjacency_list)

print(f"PART A: the number of paths to the end is {len(paths_to_end)}")

# PART B: same but now allowed to visit a single small cave at most twice

def get_path_to_end_b(n, adj_list, use_twice):
    # use_twice = list of length len(nodes) which is zero for all nodes that can be used
    # only once, one for a node that may be used twice

    if n == "end":
        return [['end']]

    else:
        children_of_n = adj_list[n]

        if n.islower() and use_twice[n] == 0:
            # can't come back here, remove n from the adjacency list
            adj_list = {k:[ch for ch in v if ch != n] for k,v in adj_list.items() if k != n}

        if use_twice[n] == 1:
            use_twice = {node:0 for node in use_twice}

        child_paths = [path for child in children_of_n for path in get_path_to_end_b(child, adj_list, use_twice)]

        return [[n, *path] for path in child_paths]

# this is extremely inefficient but recalculate all paths every time and only save the ones 
# with a particular node used twice
use_twice_dict = {n:0 for n in all_nodes}
all_paths = get_path_to_end('start', adjacency_list)
lowercase_nodes = [node for node in all_nodes if node.islower() and not node in ['start', 'end']]

for n in lowercase_nodes:

    use_twice_dict[n] = 1 
    new_paths = get_path_to_end_b('start', adjacency_list, use_twice_dict)

    new_paths_with_doublen = [path for path in new_paths if path.count(n)==2]
    all_paths.extend(new_paths_with_doublen)

    use_twice_dict[n] = 0


print(f"PART B: the number of paths to the end allowing 2x small cave visits is {len(all_paths)}")


        # more readable version of the part A list comprehension
        # child_paths = []
        # for child in children_of_n:
        #     possible_child_paths = get_path_to_end(child, adj_list)
        #     for path in possible_child_paths:
        #         child_paths.append(path)