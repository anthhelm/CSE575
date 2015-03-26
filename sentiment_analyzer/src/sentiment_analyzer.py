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

