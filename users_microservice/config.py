from pymongo import MongoClient

client = MongoClient("mongodb://neutron1:lolfool1@172.28.128.13/usersmicroservice")
db = client["usersmicroservice"]

ip_port = '127.0.0.1:5000'