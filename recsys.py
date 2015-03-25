'''
(mkdir -p ~/.graphlab && echo -e "[Product]\nproduct_key=D88D-A354-757A-35A2-7039-BFA6-AE28-A612" > ~/.graphlab/config && echo "Configuration file written") || echo "Configuration file not written"
'''

# prototype recommender in python
# uses amazon_mahout.csv
import numpy as np
import pandas as pd
from scipy.stats import pearsonr
import math

model = pd.read_csv('preprocessfinal.csv')
model = pd.read_csv('amazon_mahout.csv')




def items_rated_by(user):
    return list(model[model.UserID == user].ProductID)

def common_to_both(user1, user2):
    return list(set(items_rated_by(user1)) & set(items_rated_by(user2)))

def similarity(user1, user2):
    user1_reviews, user2_reviews = [],[]
    
    for product_id in common_to_both(user1,user2):

        review_from_user1 = model[((model.UserID == user1) & (model.ProductID == product_id))].Review.values[0]
        review_from_user2 = model[((model.UserID == user2) & (model.ProductID == product_id))].Review.values[0]
        
        user1_reviews.append(review_from_user1)
        user2_reviews.append(review_from_user2)
    
    if len(user1_reviews) > 0:
        coeff, p = pearsonr(user1_reviews, user2_reviews)
        return 0 if math.isnan(coeff) else coeff
    else:
        return 0
    
    
def k_neighborhood(user,k):
    user_list = list(model.UserID.unique())
    user_list.remove(user)
    sim_array = []
    
    i = 0
    print("need to check against %d users" % len(user_list))
    
    for other_user in user_list:
        i += 1
        if (i % 1000 == 0):
            print("on user #%d" % i)
        similarity(user, other_user)
    return 0
    

import time
import random

t0 = time.time()
for i in range(10000):
    #similarity(3,5)
    pearsonr([1,5,1,5,2,3,5],[1,4,5,5,4,1,2])
t1 = time.time()

print t1-t0
