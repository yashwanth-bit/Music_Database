from pymongo import MongoClient
from getpass import getpass
from py2neo import Graph
import pandas
import redis
import secrets

try: 
    conn = MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 

r = redis.Redis(host='127.0.0.1',port=6379, db=0)

#connection to neo4j database
graph = Graph(host='localhost', port=7687, password="1234")

