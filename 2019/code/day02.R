setwd(dirname(parent.frame(2)$ofile))
library(data.table)
data <- "../data/day02.csv"

# part 1 ----

# function to process data, adjusting for R indexing from 1
process_ints <- function(vec, start = 0) {
    cur_int = vec[start+1]
    
    if (cur_int == 99) return(vec[0+1])
    
    # prep the rest of the arguments. no error catching....whatever.
    arg1_ind = vec[start+1+1]
    arg2_ind = vec[start+2+1]
    arg1 = vec[arg1_ind+1]
    arg2 = vec[arg2_ind+1]
    result_ind = vec[start+3+1]
    next_start = start + 4
    
    if (cur_int == 1) {        # sum
        vec[result_ind+1] = arg1+arg2
        process_ints(vec, next_start)
    } else if (cur_int == 2) { # multiply
        vec[result_ind+1] = arg1*arg2
        process_ints(vec, next_start)
    }  else {                  # error
        stop(paste0("ünrecognized int: ", cur_int, " at ", start)) 
    }
}

# read in data
ints <- transpose(fread(data))$V1

# replace position 1 with 12 and position 2 with 2 (account for indexing from 1)
ints[1+1] <- 12
ints[2+1] <- 2

# run function
process_ints(ints)

# part 2 ----

# brute force
noun_verb_bruteforce <- function(vec, goal) {
    test_vec = vec
    max_index = length(test_vec) - 1
    
    for (noun in 0:max_index) {
        for (verb in 0:max_index) {
            
            test_vec[1+1] <- noun
            test_vec[2+1] <- verb
            index0 = process_ints(test_vec)
            
            # check if done. if not, start over
            if (index0 == goal) {
                return(c(noun = noun, verb = verb))
            } else {
                test_vec = vec
            }
        }
    }
}

nounverb <- noun_verb_bruteforce(ints, 19690720)

nounverb['noun']*100 + nounverb['verb']
