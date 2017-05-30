import pymongo


class Database(object):
    URI = ""
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        Database.DATABASE[collection].find_one(query)