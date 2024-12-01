import math 

f = open("../data/day02.dat")
input = f.readlines()


# ----------------------------------------------------------------------------|
# part 1
# ----------------------------------------------------------------------------|

# functions
def restructure_data(lines):

    games = []
    for game in lines:

        game_dict = {}
        data = game.strip().split(": ")
        
        game_dict["id"] = int(data[0].split(" ")[1])

        game_dict["pulls"] = [{numcol.split(" ")[1]:int(numcol.split(" ")[0]) \
                                for numcol in pull.split(", ")} \
                                for pull in data[1].split("; ")]

        games.append(game_dict)

    return games


def add_maxes(games, compare_dict):
    all_colors = compare_dict.keys()

    # get maxs pulls of each color per game
    for game in games:
        maxes = {color:0 for color in all_colors}

        for pull in game["pulls"]:
            for color,num in pull.items():
                if num > maxes[color]:
                    maxes[color] = num

        # remove any zeros
        maxes = {col:num for col,num in maxes.items() if num > 0 }
        
        # add to the record
        game['maxes'] = maxes
    

def sum_possible(games, compare_dict):

    # check which games are possible and sum ids
    id_sum = 0
    for game in games:

        possible = True
        for color,num in game["maxes"].items():
            if num > compare_dict[color]:
                possible = False
        if possible == True:
            id_sum += game["id"]

    # return sum of ids
    return id_sum


# work
elf_params = {'red':12 , 'green':13, 'blue':14}
all_games = restructure_data(input)
add_maxes(all_games, elf_params)
total = sum_possible(all_games, elf_params)

print(f"part 1: the total ids of possible games is {total}")


# ----------------------------------------------------------------------------|
# part 2
# ----------------------------------------------------------------------------|

def compute_power(games):
    all_powers = [math.prod(game['maxes'].values()) for game in games]
    sum_of_powers = sum(all_powers)

    return sum_of_powers

total_power = compute_power(all_games)
print(f"part 2: the total powers of minimum games is {total_power}")
