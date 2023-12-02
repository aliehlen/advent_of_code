# data
data_file = "../data/day02.dat"

# rock paper scissors
#  A    B     C

# read data
data = [[n for n in l.split(" ")] for l in open(data_file, 'r').read().split("\n")]

# part 1
play_scores = {'X': 1, 'Y': 2, 'Z': 3}
outcome = {'X': {'A':3, 'B':0, 'C':6}, 
           'Y': {'A':6, 'B':3, 'C':0}, 
           'Z': {'A':0, 'B':6, 'C':3}}

score = sum([outcome[r[1]][r[0]] + play_scores[r[1]] for r in data])

print(f"the total score is {score}")

# part 2
play_scores = {'A': 1, 'B': 2, 'C': 3}
outcome_scores = {'X': 0, 'Y': 3, 'Z': 6}
my_play = {'X': {'A':'C', 'B':'A', 'C':'B'}, 
           'Y': {'A':'A', 'B':'B', 'C':'C'}, 
           'Z': {'A':'B', 'B':'C', 'C':'A'}}

new_score = sum([play_scores[my_play[r[1]][r[0]]] + outcome_scores[r[1]] for r in data])

print(f"the total score is {new_score}")