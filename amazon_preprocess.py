#!/usr/local/bin/python
'''
========================================================================================================
filename: amazon_preprocess.py
version: 0.1
date: 3/15/2015
author: Anthony Helmstetter
description: 
    Converts amazon user review data from single line .txt
    to tab delimited .csv. Each row in the .csv corresponds to one
    review/record, where columns are the features provided by amazon.
    Features are productId, title, price, userId, profileName, 
    helpfulness, score, time, summary, text.  


use: 
    Change python variable file_name to point to the filename of the data
    set you'd like to convert. Options are commented for convenience. 
    Make sure you untar the amazon data sets and have the corresponding
    .txt file in the same directory before running.


todo: 
    I haven't done much testing to verify the csv is as it should be. The file is too large to open in Excel,
    but I was able to open the .csv in Vi and visually confirm the format. Might be more difficult if we move on to 
    larger data sets > 1gig, in which case we should more to a DB, or implement some checks in the conversion code.
    

========================================================================================================
'''

# set up file names and file handlers, write headers to output csv
file_name = 'Amazon_Instant_Video'

f_in  = file_name + '.txt'
f_out = file_name + '.csv'
fout = open(f_out,'w')
fout.write('productId\t title\t price\t userId\t profileName\t helpfulness,\t score\t time\t summary\t text\n') 

i = 0
print("reading data...")


# open input txt file, and read lines
with open(f_in,'r') as f:

    
    # read in lines one at a time
    content = f.readlines()
    
    for line in content:

        # display line progress
        i = i + 1
        if (i % 1000000) == 0: 
            print('processing line number %d: ' % i)


        # split each line of .txt file on ':', to store feature_name and feature_value in list
        sline = line.split(': ',1)

        # skip over newlines in input .txt
        if len(sline) < 2:
            fout.write('\n') 

        # write feature_name and feature_value separated by tabs in output csv
        else:
            if sline[0] == 'product/productId':
                fout.write(sline[1].strip())
            else:
                fout.write('\t' + sline[1].strip())


# close file handles
f.closed
fout.close() 
print("done.")