import pymongo

def accessCollection(connectionString, dbName, collectionName):
    myclient = pymongo.MongoClient(connectionString)
    mydb = myclient[dbName]
    mycol = mydb[collectionName]
    return mycol

def insertCollectionItem(mycol, data):
    x = mycol.insert_one(data)
    return x

def emptyCollection(mycol):
    x = mycol.remove()
    return x