from pymongo import MongoClient
from singleton import singleton
from flask import Flask
from flask_pymongo import PyMongo

@singleton
class DBManager :
    # name = 'gestionale2022_2'
    # host =  'localhost'#'192.168.178.74'  #'172.20.10.2'
    # port = 27017
    # client = MongoClient(host=host , port=port , connect=True)
    # db = client[name] #oppure client.gestionale2022_2 => non uso questa notazione poichè presente un underscore

    app = Flask(__name__)
    app.config["MONGO_URI"] = 'mongodb://127.0.0.1:27017/gestionale2022_2'
    mongo = PyMongo(app)
    db = mongo.db



    def insert (self , collection , mymap):
        collection.insert_one(mymap)

    def update(self, collection, searchKeysValuesPairs, changedKeysValuesPairs):
        collection.update_one(searchKeysValuesPairs, {'$set' : changedKeysValuesPairs})

    def readAll(self, collection):
        return collection.find('{}')

    # def readAll(self , collection):
    #     elements = []
    #     cursor = collection.find('')
    #     for document in cursor:
    #         elements.append(document)
    #     return elements


    def read(self, collection, searchKeysValuesPairs):
        return collection.find(searchKeysValuesPairs)

    def readOne(self, collection, idToken):
        return collection.find_one({'idToken':idToken})

    def delete(self, collection, idToken):
        collection.delete_one({'_id': idToken})

