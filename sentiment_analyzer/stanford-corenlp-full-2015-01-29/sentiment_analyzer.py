#!/usr/local/bin/python
'''
========================================================================================================
filename: amazon_preprocess.py
version: 0.1
date: 3/26/2015
author: Prajwal Paudyal

description: 
    Uses the output of amazon_preprocess.py file's output
    1. Creates column titles
    2. Adds columns for Summary Sentiment and Review Sentiment
    3. Uses Stanford NLP  Sentiment Analyzer (http://nlp.stanford.edu/sentiment/code.html) to get a 5 class labelled sentiment score on the review summary
    4. Uses Same to get line by line sentiment score on the actual review and averages this to obtain a single 5 class value for sentiment score
    5. Combines these scores by giving 2:1 weight on Summary vs. Review text
    6. Appends final review score from 0 - 5 as a separate column in the csv file.


use: 
    


todo: 
    1. 
    

========================================================================================================
'''

import csv
import re 
from _sqlite3 import Row
from docutils.utils.math.math2html import Newline
from random import randint
import os
import subprocess
from pyspark import SparkContext


def sentence_analyzer(sentence):
       score = 3
       command = "echo" + ' "' + sentence + '"' + " | java -cp '*' -mx5g edu.stanford.nlp.sentiment.SentimentPipeline -stdin " 
       print command
       out = os.popen(command).read()
       print "program output:", out  
       if "Negative" in out : score = 2
       if "Very negative" in out : score = 1
       if "Neutral" in out : score = 3
       if "Positive" in out : score = 4
       if "Very positive" in out : score = 5
       return score


def block_analyzer(review):
    total_score = 0
    counter = 0 
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', review)
    for sentence in sentences:
        counter += 1
        if(not sentence.isspace() and sentence):
            sentence_score = sentence_analyzer(sentence)
            total_score = total_score + sentence_score
    return total_score/counter


def NLP():
	with open(f_in,'rb') as csvfile:
		mcsv = csv.reader(csvfile, delimiter='\t')
		for row in mcsv:
			summary_score = block_analyzer(row[2])
			review_score = block_analyzer(row[3])
			print summary_score
			score = (1.2*summary_score + 0.8*review_score)/4.0
			print score
			fout.write("%s\t%s\t%d\t%d\t%f\t\n" % (row[0],row[1],summary_score, review_score, score))    
	fout.close() 

# with open(filename, 'rb') as csvfile:
#     counter = 0
#     final_score = []
#     mcsv = csv.reader(csvfile, delimiter='\t')
#     for row in mcsv:
#         print row[0] + ":" + row[1] + ":" + row[2] + ":" + row[3] 
#         counter += 1
#         summary_score = block_analyzer(row[2]) 
#         review_score = block_analyzer(row[3])
#         final_score.append( (2*summary_score + review_score)/3) 
#         #print str(summary_score)  +  str(review_score) + str(final_score)
#     #print final_score
if __name__ == "__main__":
	if 'sc' not in globals():
		sc = SparkContext('local[4]', 'pyspark')
	file_name_ouput = 'OutputNLP'
	file_name_input = 'PreprocessFinal_NLP_head'

	f_in  = file_name_input + '.csv'
	f_out = file_name_ouput+ '.csv'

	fout = open(f_out,'a')

	#run code
	NLP()

    
