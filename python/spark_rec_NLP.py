#Prajwal Paudyal
#Creates normalized NLP values (


import csv

        
file_name_ouput = '../csvFiles/spark_input_NLP_Normalized'
file_name_input = '../csvFiles/spark_input'

f_in  = file_name_input + '.csv'
f_out = file_name_ouput+ '.csv'


#MAXIMUM SIZE OF ADJUSTMENT


fout = open(f_out,'a')

def normalize_nlp(nlp):
	return 2*nlp +3


def combile_NLP(raw, nlp, alpha):
	combined = raw + alpha*(normalize_nlp(nlp) - raw)/4
	return combined


with open(f_in,'rb') as csvfile:
	mcsv = csv.reader(csvfile, delimiter=',')
	for row in mcsv:
		fout.write("%s,%s,%s,%s,%f,%f,%f,%f\n" % (row[0],row[1], row[2], row[3], normalize_nlp(float(row[3])),combile_NLP(float(row[2]), float(row[3]), 1.0), combile_NLP(float(row[2]), float(row[3]), 0.75), combile_NLP(float(row[2]), float(row[3]), 0.5)))
	fout.close()