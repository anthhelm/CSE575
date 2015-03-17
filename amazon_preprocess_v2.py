import csv
import pandas as pd
import numpy as np
import pylab as pl

file_name = 'Amazon_Instant_Video'

f_in  = file_name + '.txt'
f_out = file_name + '.csv'
fout = open(f_out,'w')


print("reading data...")
# open input txt file, and read lines
with open(f_in,'r') as f:

    reviews = []
    temp = []
    # read in lines one at a time
    for line in f:
        if line == "\n":
            reviews.append(temp)
            temp = []
        else:
            entry = line.split(": ",1)[1].strip()
            temp.append(entry.replace(',',''))

f.closed

#verify 
for record in reviews:
    if len(record) != 10:
        print("error!")

#write
print("writing csv...")
fout.write('productId, title, price, userId, profileName, helpfulness, score, time, summary, text\n') 
with open(f_out, "wb") as f:
    writer = csv.writer(f,delimiter=',',
                            quotechar="'", quoting=csv.QUOTE_MINIMAL)
    writer.writerows(reviews)

f.close()


# pandas
print("creating data frame...")
df = pd.read_csv("Amazon_Instant_Video_Sample.csv", sep=',')
print(df.head())
