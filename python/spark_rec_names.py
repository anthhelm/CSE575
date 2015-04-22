from pyspark.mllib.recommendation import ALS, Rating, MatrixFactorizationModel
from pyspark import  SparkContext
import pandas as pd
import numpy as np
import sys, random, itertools
import csv

# generate new CSVs for 5 Fold CV and final testing set


def predict_movie_names(userid,rank, numIterations, reg,sc,noOfPredictions):
    #Read User and movie names Dictionaties
    All_Movies=[]
    top_k_movies=[]

    reader3 = csv.reader(open('items_int.csv', 'rb'))
    movies_int = dict(x for x in reader3)


    reader1 = csv.reader(open('final_movies_dict.csv','rb'))
    movie_names = dict(x for x in reader1)

    reader2 = csv.reader(open('final_users_dict.csv','rb'))
    user_names = dict(x for x in reader1)


    for each in movies_int.values():
        All_Movies.append((userid,each))
    if userid not in user_names:
        print "Beeep!! Error!!"
    
    #print All_Movies
    
    All_Movies_RDD=sc.parallelize(All_Movies)
    
    data_train = sc.textFile("final_train.csv") 
    data_test = sc.textFile("final_test.csv") 

    ratings_train = data_train.map(lambda l: l.split(',')).map(lambda l: Rating(int(l[0]), int(l[1]), float(l[2])))
    ratings_test = data_test.map(lambda l: l.split(',')).map(lambda l: Rating(int(l[0]), int(l[1]), float(l[2])))

    model = ALS.train(ratings_train, rank, numIterations, lambda_ = reg)
    test_predictions = model.predictAll(All_Movies_RDD).map(lambda r: (r[2], r[1])).sortByKey(0)

    final_predictions=test_predictions.take(noOfPredictions)

    for each in final_predictions:
	    prediction=movie_names.get(str(each[1]))
	    top_k_movies.append(prediction)	

    return top_k_movies    



if __name__ == "__main__":

    if 'sc' not in globals():
	    sc = SparkContext('local[4]', 'pyspark')

	    top_k_movies = predict_movie_names('12624',80,20,0.15,sc,5)
	     
	    print "******************************" 
	    for each in top_k_movies:
	    	print each
        
	    
    
        
	
    


