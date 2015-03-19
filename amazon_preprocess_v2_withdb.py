import csv
#import pandas as pd
#import numpy as np
#import pylab as pl
import psycopg2

DATABASE_NAME="sml"

def getopenconnection():
    print "in this function"
    print psycopg2.connect(dbname="sml",user="postgres",host="localhost")

"""
    We create a DB by connecting to the default user and database of Postgres
    The function first checks if an existing database exists for a given name, else creates it.
    :return:None
    """

def create_db(dbname):
    # Connect to the default database
    con = getopenconnection()
    con.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()

    # Check if an existing database with the same name exists
    cur.execute('SELECT COUNT(*) FROM pg_catalog.pg_database WHERE datname=\'%s\'' % (dbname,))
    count = cur.fetchone()[0]
    if count == 0:
        cur.execute('CREATE DATABASE %s' % (dbname,))  # Create the database
    # Clean up
    cur.close()
    con.close()

def load_into_db(conn,amazontablename):
    cur=openconnection.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS %s(
                   productid VARCHAR NOT NULL, TITLE VARCHAR NOT NULL, PRICE FLOAT NOT NULL,USERID VARCHAR NOT NULL,Profilename VARchar NOT NULL,HELPFULNESS CHAR NOT NULL,SCORE FLOAT NOT NULL,SUMMARY VARCHAR NOT NULL,TEXT VARCHAR NOT NULL ); """%(amazontablename))
    file_name = 'Amazon_Instant_Video'
    f_in  = file_name + '.txt' 
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
    
    for review in reviews:
        if len(review)!=9:
            print "Error.Length of review is less than 10!!"
        cur.execute(" Insert INTO %s(productid,title,price,userid,profilename,helfulness,score,summary,text) VALUES(%s,%s,%s,%f,%s,%s,%s,%f,%s,%s) "%(amazontablename,review[0],review[1],review[2],review[3],review[4],review[5],review[6],review[8],review[9]));     
    f.closed


if __name__ == '__main__':
    create_db(DATABASE_NAME)
    try:    
	with getopenconnection() as conn:
        load_into_db();
    except Exception as detail:
        print "OOPS! This is the error ==> ", detail



