import csv

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

#cleaningup 
for record in reviews:
    if len(record) != 10:
        reviews.remove(record)

with open("preprocessinter.csv","wb") as f:
    fieldnames = ['ProductId', 'UserId','Score','TextReview']
    writer=csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    for record in reviews:
        writer.writerow({'ProductId':record[0],'UserId':record[3],'Score':record[6],'TextReview':record[9]})
f.close()    
  

