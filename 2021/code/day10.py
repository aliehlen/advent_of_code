# data
data_file = "../data/day10.txt"

# read in data and split it into number draws and boards

import numpy as np
data = open(data_file, 'r').read().split('\n')

# PART A: get first illegal characters

points = {"]":57, ")":3, "}":1197, ">":25137}
openers = ["[", "(", "{", "<"]
closers = ["]", ")", "}", ">"]

# use a stack to parse each line: 
illegal_closers = []
incomplete_lines = []

for i,line in enumerate(data):
    stack = []
    for char in line:
        if char in openers:
            stack.append(char)
        elif char in closers:
            if stack[-1] == openers[closers.index(char)]:
                stack.pop()
            else:
                illegal_closers.append(char)  
                break
    else:
        if len(stack) > 0:
            incomplete_lines.append(i)

score = sum(points[illegal] for illegal in illegal_closers)

print(f"PART A: the total score of illegal closers is {score}")

# PART B: what is the score of completing the incomplete lines?

scores = []
points_b = {"]":2, ")":1, "}":3, ">":4}

for i in incomplete_lines:
    line = data[i]

    # do same parsing, but now don't have to worry about illegal closers
    stack = []
    for char in line:
        if char in openers:
            stack.append(char)
        elif char in closers:
            if stack[-1] == openers[closers.index(char)]:
                stack.pop()

    needed_closers = [closers[openers.index(open)] for open in stack[::-1]] 

    line_score = 0
    for closer in needed_closers:
        line_score = 5*line_score + points_b[closer]

    scores.append(line_score)

scores.sort()
middle_score = scores[int((len(scores)-1)/2)]


print(f"PART B: the middle score of incomplete lines is {middle_score}")

