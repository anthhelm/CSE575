#!/usr/local/bin/python

# set up file names and file handlers, write headers to output csv
file_name = 'Amazon_Instant_Video'

f_in  = file_name + '.txt'
f_out = file_name + '.csv'
fout = open(f_out,'w')


j = 1
r = 0
item_int = 1
user_int = 1

item_d = {'unknown': -1}
user_d = {'unknown': -1}


# open input txt file, and read lines
with open(f_in,'r') as f:
    #content = f.readlines()
    for line in f:

        lnum = (j % 11 )
        if lnum == 1:
            item = line.split(': ',1)[1].strip()

            if item in item_d:
                item = item_d[item]
            else:
                item_d[item] = item_int
                item = item_int
                item_int = item_int + 1


        elif lnum == 4:
            user = line.split(': ',1)[1].strip()

            if user in user_d:
                user = user_d[user]
            else:
                user_d[user] = user_int
                user = user_int
                user_int = user_int + 1



        elif lnum == 7:
            score = line.split(': ',1)[1].strip()
        elif lnum == 0 and user != -1:
            r = r + 1
            if (r % 10000 == 0):
                print r
            fout.write(str(user) + ',' + str(item) + ',' + score + '\n')
        j = j + 1



fout.close() 
print("done.")
