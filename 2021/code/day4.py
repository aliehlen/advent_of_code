# data
data_file = "../data/day4.txt"

import numpy as np

# return index of winning boards, if there are any
def any_won(res, size=5):
    winning_indices = []

    for i,b in enumerate(res):
        rows = np.sum(b, axis=1)
        cols = np.sum(b, axis=0)
        
        if np.any(rows == size) or np.any(cols == size):
            winning_indices.append(i)
    
    if len(winning_indices) == 0:
        return "no winner yet"
    else:
        return winning_indices


# read in data and split it into number draws and boards
data = open(data_file, 'r').read().split('\n\n')

draws = [int(d) for d in data[0].split(',')]
boards = np.array([[[int(n) for n in ln.split()] for ln in brd.split('\n')] for brd in data[1:]])

# PART A: what is the score of the first board to win?

# play bingo! see who won
results = np.zeros_like(boards)

for draw in draws:
    results[boards == draw] += 1
    winners = any_won(results)

    if isinstance(winners[0], int):
        # print winning score - there has to be only one 
        winner = winners[0]

        winning_board = boards[winner]
        winning_result = results[winner]

        unmarked = sum(winning_board[winning_result == 0])
        print(f"PART A: the final score is {unmarked*draw}")
        break

# PART B: what is the score of the last board to win?

# now we have to keep track of the last board to have won
results = np.zeros_like(boards)

prev_win_score = 0
prev_win_board = np.array([])
prev_win_results = np.array([])

for draw in draws:
    results[boards == draw] += 1
    winners = any_won(results)

    if isinstance(winners[0], int):

        if len(winners) == 1:
            # this question doesn't make sense if there are multiple
            # winners, only bother to save the score if there's one
            winner = winners[0]  

            prev_win_board = boards[winner]
            prev_win_results = results[winner]
            unmarked = sum(prev_win_board[prev_win_results == 0])
            prev_win_score = unmarked*draw

        boards = np.delete(boards, winners, axis=0)
        results = np.delete(results, winners, axis=0)

print(f"PART B: the final score of the last board is {prev_win_score}")