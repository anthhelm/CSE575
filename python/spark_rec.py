from pyspark.mllib.recommendation import ALS, Rating, MatrixFactorizationModel
from pyspark import  SparkContext
import sys, random, itertools
import pandas as pd
import numpy as np


generate_csv = 1
re_build = 1
if 'sc' not in globals():
        sc = SparkContext('local[4]', 'pyspark')

fout = open('results.txt','w')
fout.write("rank,num_iterations,lambda,training cv MSE, testing cv MSE\n")

if generate_csv == 1:
	random.seed(1)

	df = pd.read_csv("Amazon_Instant_Video.csv", sep=',', names=['userid','movieid','score'])
	#df = pd.read_csv("movielens.csv", sep=',', names=['userid','movieid','score'])


	byuserid = df.groupby('userid').aggregate(np.count_nonzero)
	tags = byuserid[byuserid.score >= 10].index
	df = df[df['userid'].isin(tags)]


	rows = random.sample(df.index, len(df.index))
	k = 5
	n = len(df.index) / 5
	sample1 = rows[0:n]
	sample2 = rows[n:2*n]
	sample3 = rows[2*n:3*n]
	sample4 = rows[3*n:4*n]
	sample5 = rows[4*n:]

	samples = [sample1, sample2, sample3, sample4, sample5]
	i = 0
	for sample in samples:
	    i += 1
	    df_test = df.ix[sample]
	    df_train = df.drop(sample)
	    df_test.to_csv('test_' + str(i) + '.csv',sep=',', header=False, index=False)
	    df_train.to_csv('train_' + str(i) + '.csv',sep=',', header=False, index=False)




if re_build == 1:
	rank_vec = [40]
	numIterations_vec = [20]
	reg_vec = [0.0000001,.000005]

	err_train = []
	err_test = []

	err_test_cv = []
	err_train_cv = []



	for rank, numIterations, reg in itertools.product(rank_vec, numIterations_vec, reg_vec):
		for i in range(1,6):
			data_train = sc.textFile("/Users/aechelm/Documents/recommender/train_" + str(i) + ".csv") 
			data_test = sc.textFile("/Users/aechelm/Documents/recommender/test_" + str(i) + ".csv") 

			ratings_train = data_train.map(lambda l: l.split(',')).map(lambda l: Rating(int(l[0]), int(l[1]), float(l[2])))
			ratings_test = data_test.map(lambda l: l.split(',')).map(lambda l: Rating(int(l[0]), int(l[1]), float(l[2])))


			model = ALS.train(ratings_train, rank, numIterations, lambda_ = reg)

			train_data = ratings_train.map(lambda p: (p[0], p[1]))
			train_predictions = model.predictAll(train_data).map(lambda r: ((r[0], r[1]), r[2]))
			ratesAndPreds_train = ratings_train.map(lambda r: ((r[0], r[1]), r[2])).join(train_predictions)
			MSE_train = ratesAndPreds_train.map(lambda r: (r[1][0] - r[1][1])**2).reduce(lambda x, y: x + y) / ratesAndPreds_train.count()


			test_data = ratings_test.map(lambda p: (p[0], p[1]))
			test_predictions = model.predictAll(test_data).map(lambda r: ((r[0], r[1]), r[2]))
			ratesAndPreds_test = ratings_test.map(lambda r: ((r[0], r[1]), r[2])).join(test_predictions)
			MSE_test = ratesAndPreds_train.map(lambda r: (r[1][0] - r[1][1])**2).reduce(lambda x, y: x + y) / ratesAndPreds_test.count()

			err_test.append(MSE_test)
			err_train.append(MSE_train)

			#print("MSE Training Data = " + str(MSE_train))
			#print("MSE Testing Data = " + str(MSE_test))


		err_test_cv.append(sum(err_test) / len(err_test))
		err_train_cv.append(sum(err_train) / len(err_train))

		fout.write("%d,%d,%f,%f,%f\n" % (rank, numIterations, reg, err_train_cv[-1], err_test_cv[-1]))

		err_test = []
		err_train = []

		#model.save(sc, "model_rank_100_iter_20")

	else:
		model = MatrixFactorizationModel.load(sc, "model_rank_100_iter_20")
		print("model loaded")


# p1 = model.predict(2257,82)#,5.0
# p2 = model.predict(2125,82)#,4.0
# p3 = model.predict(474,82)#,5.0
# p4 = model.predict(2275,82)#,2.0
# p5 = model.predict(16,82)#,1.0
# p6 = model.predict(2280,83)#,5.0
# print(p1,p2,p3,p4,p5,p6)

print "======================================================"
print zip(err_train_cv, err_test_cv)
print "======================================================"