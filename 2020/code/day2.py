import pandas as pd
import numpy as np

data_file = "../data/day2.txt"
data = pd.read_csv(data_file, sep=" ", names=['range', 'letter', 'pw'])

# clean data: get letter alone, make range numeric and in diff columns
data['letter'].replace(":", "", regex=True, inplace=True)

data[['lowerb', 'upperb']] = data['range'].str.split("-", expand=True)
data['lowerb'] = data['lowerb'].astype(int)
data['upperb'] = data['upperb'].astype(int)

# part 1 - how many passwords are valid where range is # instances

data['letter_count'] = np.char.count(data['pw'].to_numpy(dtype='str'), 
                                     data['letter'].to_numpy(dtype='str'))
									 
data['valid_pw_p1'] = (data['letter_count'] >= data['lowerb']) & \
                      (data['letter_count'] <= data['upperb'])

print(f"The number of valid passwords is {np.sum(data['valid_pw_p1'])}")

# part 2 - how many passwords are valid where range is position of letters

data['first_ind'] = [word[i-1] for word,i in zip(data['pw'], data['lowerb']) ]
data['second_ind'] = [word[i-1] for word,i in zip(data['pw'], data['upperb']) ]

data['valid_pw_p2'] = (data['letter'] == data['first_ind']) ^ \
                      (data['letter'] == data['second_ind'])
					  
print(f"The number of valid passwords is {np.sum(data['valid_pw_p2'])}")