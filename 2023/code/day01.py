import re

f = open("../data/day01.dat")
input = f.readlines()


# ----------------------------------------------------------------------------|
# part 1
# ----------------------------------------------------------------------------|

# functions
def sum_firstlasts(lines):

    numbers = [[char for char in line if char.isnumeric()] for line in lines]
    numbers = [int(num[0]+num[-1]) if len(num) > 0 else 0 for num in numbers]

    return sum(numbers)


# work
total = sum_firstlasts(input)
print(f"part 1: the sum of the numbers is {total}")


# ----------------------------------------------------------------------------|
# part 2
# ----------------------------------------------------------------------------|

# functions
def sub_numbers(line, number_words):
    
    line_list = list(line)

    for number_word, number in number_words.items():
        # this doesn't work if they overlap but they can't
        number_ind = [match.start() for match in re.finditer(number_word, line)]
        
        for ind in number_ind:
            line_list[ind] = str(number) 

    return ''.join(line_list)    


# work
number_dict = {"one": 1, "two": 2, "three": 3, "four": 4, 
               "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

lines_subbed = [sub_numbers(line, number_dict) for line in input]
total_part2 = sum_firstlasts(lines_subbed)

print(f"part 2: the sum of the numbers is {total_part2}")
