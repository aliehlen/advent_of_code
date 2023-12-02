# data
data_file = "../data/day05.dat"

# prep
import collections
import string
import copy

# read data
data = [chunk for chunk in open(data_file, 'r').read().split("\n\n")]

# split up and reorder stacks so they are actually stacks
stacks_prep = [line for line in data[0].split("\n")]
stacks_prep = [[line[col] for line in stacks_prep] for col in range(len(stacks_prep[-1]))]
stacks_prep = [stack[::-1] for stack in stacks_prep if stack[-1].isnumeric()]
stacks_prep = [collections.deque([item for item in stack if item in string.ascii_uppercase]) for stack in stacks_prep]

# instructrions are: number to move, stack from, stack to
instructions = [[int(word) for word in line.split() if word.isnumeric()] for line in data[1].split("\n")]

# part 1
stacks = copy.deepcopy(stacks_prep)

for instruction in instructions:

    number_to_move = instruction[0]
    stack_from = instruction[1] - 1
    stack_to = instruction[2] - 1

    for i in range(instruction[0]):
        stacks[stack_to].append(stacks[stack_from].pop())

top_of_all_stacks = ''.join([stack.pop() for stack in stacks])

print(f"the crates on top of all stacks are: {top_of_all_stacks}")

# part 2
stacks = copy.deepcopy(stacks_prep)

for instruction in instructions:

    number_to_move = instruction[0]
    stack_from = instruction[1] - 1
    stack_to = instruction[2] - 1

    crates_to_move = []
    for i in range(instruction[0]):
        crates_to_move.append(stacks[stack_from].pop())

    stacks[stack_to].extend(crates_to_move[::-1])

top_of_all_stacks = ''.join([stack.pop() for stack in stacks])

print(f"the crates on top of all stacks using the CrateMover9001 are: {top_of_all_stacks}")

