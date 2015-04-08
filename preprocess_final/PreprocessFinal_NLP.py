file_name_ouput = 'PreprocessFinal_NLP'
file_name_input = 'Amazon_Instant_Video'

f_in  = file_name_input + '.txt'
f_out = file_name_ouput+ '.csv'
fout = open(f_out,'a')
linenumber=long(1)
ReviewID=long(1)
#fout.write('ReviewID,productid,title,price,userid,profilename,helfpulness,score,time,summary,text\n')
userid=''

with open(f_in,'r') as f:
    for line in f: 
        lnum= (linenumber % 11)
        #print lnum
        #if lnum == 1:
        #    productid = line.split(':',1)[1].strip('\n')
        #elif lnum == 2:
        #    title = line.split(':',1)[1].strip('\n')
        #elif lnum == 3:
        #    price  = line.split(':',1)[1].strip('\n')
        if lnum == 4:
            userid = line.split(':',1)[1].strip('\n')
        #elif lnum == 5:
        #    profilename = line.split(':',1)[1].strip('\n')
        #elif lnum == 6:
        #    helfpulness = line.split(':',1)[1].strip('\n')
        elif lnum == 7:
            score = line.split(':',1)[1].strip('\n')
        #elif lnum == 8:
        #    time = line.split(':',1)[1].strip('\n')
        elif lnum == 9:
            summary = line.split(':',1)[1].strip('\n')
        elif lnum == 10:
            reviewtext = line.split(':',1)[1].strip('\n') 
        elif lnum == 0:
           if userid is not 'unknown':
               #print ReviewID
               fout.write("%d,%d,%s,%s\n" % (ReviewID,int(str(score).strip('.0')),summary,reviewtext))
               ReviewID = ReviewID+1
        linenumber += 1
fout.close()
           
