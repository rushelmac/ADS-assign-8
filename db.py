import pymongo
from bson import ObjectId

class Database:
    # CONNECT TO LOCAL DATABASE
    # connection = pymongo.MongoClient("localhost", 27017)
    
    #CONNECT TO CLOUD DATABASE
    # collection = pymongo.MongoClient("mongodb+srv://TeamThailaiva:<1234abcd>@cluster0.xnpzq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    connection = pymongo.MongoClient("localhost", 27017)
    # CREATE DATABASE
    database = connection['ass8_database']
    # CREATE COLLECTION
    collection = database['parts']
    print("Database connected")

    def fetch(self):
        data = self.collection.find()
        return list(data)
        

    def insert(self, part, customer, retailer, price):
        document = self.collection.insert_one({"part":part, "customer": customer, "retailer": retailer, "price":price})
        return document.inserted_id

    def remove(self, id):
        document = self.collection.delete_one({'_id': ObjectId(id)})
        return document.acknowledged

    def update(self, id, part, customer, retailer, price):
        document = self.collection.update_one({'_id': ObjectId(id)}, {"$set": {"_id": id, "part":part, "customer":customer, "retailer":retailer, "price":price}})
        return document.acknowledged

    def __del__(self):
        self.connection.close()


# db = Database('store.db')
# db.insert("4GB DDR4 Ram", "John Doe", "Microcenter", "160")
# db.insert("Asus Mobo", "Mike Henry", "Microcenter", "360")
# db.insert("500w PSU", "Karen Johnson", "Newegg", "80")
# db.insert("2GB DDR4 Ram", "Karen Johnson", "Newegg", "70")
# db.insert("24 inch Samsung Monitor", "Sam Smith", "Best Buy", "180")
# db.insert("NVIDIA RTX 2080", "Albert Kingston", "Newegg", "679")
# db.insert("600w Corsair PSU", "Karen Johnson", "Newegg", "130")
