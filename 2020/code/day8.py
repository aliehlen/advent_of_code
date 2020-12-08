import pandas as pd

def run_bootcode(cmds, vals):
	
	here_before = ['no' for i in range(len(cmds))]
	accumulator = 0
	ind = 0
	any_twice = False
	
	while not any_twice:

		here_before[ind] = 'yes'
		cmd = cmds[ind]
		val = vals[ind]

		accumulator += val if cmd == "acc" else 0

		next_ind = ind + (val if cmd == "jmp" else 1)

		if next_ind == len(cmds):
			exit_code = "terminated"
			break
			
		if here_before[next_ind] == 'yes':
			any_twice = True
			exit_code = "loop"
			continue

		ind = next_ind
		
	return exit_code, accumulator

# read, use data
data_file = "../data/day8.txt"
data = open(data_file, 'r').read().split("\n")

d_cmds = [s.split(' ')[0] for s in data]
d_vals = [int(s.split(' ')[1]) for s in data]

p1_exit, p1_acc = run_bootcode(d_cmds, d_vals)
	
# part 1 - value of accumulator right before break
print(f"part 1: the value of the accumulator right before is {p1_acc}")
		
	
# part 2 

for i in range(len(d_cmds)):
	
	if d_cmds[i] == 'jmp':
		sub = 'nop'
	elif d_cmds[i] == 'nop':
		sub = 'jmp'
	elif d_cmds[i] == 'acc':
		continue
		
	exit, p2_acc = run_bootcode(d_cmds[:i]+[sub]+d_cmds[(i+1):], d_vals)
	
	if exit == "terminated":
		break
	
print(f"part 2: the value of the accumulator right before is {p2_acc}")
