#!/usr/local/bin/python
import csv

# set up file names and file handlers, write headers to output csv
#file_name_ouput = 'Movies_And_TV'

file_name_input = 'Amazon_Instant_Video'
f_in  = file_name_input + '.txt'

movie_d = {}
user_d = {}

j=1

# open input txt file, and read lines

print "Generating dictionaries.."

with open(f_in,'r') as f:
    #content = f.readlines()
    for line in f:

        lnum = (j % 11 )

	if lnum == 1:
            productid = line.split(': ',1)[1].strip()
            #print productid
 
        elif lnum == 2:
            title=line.split(': ',3)
            movie=title[2] 
            if movie not in movie_d:
                movie_d[movie]=productid  
   
        elif lnum == 4:
            user = line.split(': ',1)[1].strip()

        elif lnum == 5:
            profilename=line.split(': ',1)[1].strip()
            if profilename not in user_d:
                user_d[profilename]=user   
	j = j+1
 
items_writer = csv.writer(open('movie_names.csv', 'wb'))
for key, value in movie_d.items():
   if key is not 'unknown' and value is not 'unknown':
       items_writer.writerow([value, key])

users_writer = csv.writer(open('user_names.csv', 'wb'))
for key, value in user_d.items():
   if key is not 'unknown' and value is not 'unknown':
       users_writer.writerow([value, key])

           
#fout.close()
print "Done!!"

