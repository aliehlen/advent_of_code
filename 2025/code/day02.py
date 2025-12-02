with open("../data/day02.dat") as f:
    lines = f.read()

# first star

def find_repeat(number):
    str_number = str(number)

    for length in range(1,(len(str_number)//2) + 1) : # I overcomplicated this because I mis-read it as any repeats

        if len(str_number) % length == 0:
            splits = [str_number[i:i+length] for i in range(0,len(str_number),length)]

            if len(set(splits)) == 1 and len(splits) == 2:
                return True

ranges = [[int(val) for val in range.split("-")] for range in lines.split(",")]

repeats = []
for this_range in ranges:
    for number in range(this_range[0],this_range[1]+1):
        if find_repeat(number):
            repeats.append(number)

print(f"* the sum of invalid ids is {sum(repeats)}")

# second star

def find_repeat_second(number):
    str_number = str(number)

    for length in range(1,(len(str_number)//2) + 1) : 

        if len(str_number) % length == 0:
            splits = [str_number[i:i+length] for i in range(0,len(str_number),length)]

            if len(set(splits)) == 1 and len(splits) >= 2:
                return True
            
repeats = []
for this_range in ranges:
    for number in range(this_range[0],this_range[1]+1):
        if find_repeat_second(number):
            repeats.append(number)

print(f"** the sum of invalid ids is now {sum(repeats)}")
