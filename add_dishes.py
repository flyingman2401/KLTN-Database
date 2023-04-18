import csv, json
import databaseAccess
import sys

# Init data CSV files
dishFile =          'dishes.csv'
ingredientFile =    'ingredients.csv'
dishTypeFile =      'dishtypes.csv'

# MongoDB connection links
connectionString = "mongodb+srv://19522437:trinhtrung12@kltn-refrigerator.qbihwdd.mongodb.net/test"
collectionList = {
    "User":"",
    "Device":"",
    "SersorsData":"",
    "Rating":"",
    "Dish":"",
    "Ingredient":"",
    "DishType":"",
    "IngredientInsideFridge":"", 
    "RecommendationDishes":""
}
for item in collectionList:
    collectionList[item] = databaseAccess.accessCollection(connectionString, "RefrigeratorManagement", item)


# Initial functions

def displayProgressBar(title, count, listLength):
    sys.stdout.write('\r')
    sys.stdout.write(" |%-50s | - %s %d%%" % ('❤'*int(50/listLength*count), title, 100/listLength*count))
    sys.stdout.flush()
    
    if (count == listLength):
        print("")

def ReadDictCSV(filename):
    rowList = []
    with open(filename, encoding="utf-8-sig") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        for row in csv_reader:
            rowList.append(row)
    return rowList

def ToDishCollectionItem(rowList):
    for i in range(0, len(rowList)):
        rowList[i]['dish_ingredients'] = json.loads(rowList[i]['dish_ingredients'])
        rowList[i]['dishtype_id'] = int(rowList[i]['dishtype_id'])
    return rowList

def InitCollection(collectionName, rowList):
    databaseAccess.emptyCollection(collectionList[collectionName])    

    for i in range(0, len(rowList)):
        displayProgressBar("Init %s Collection" % collectionName, i+1, len(rowList))
        databaseAccess.insertCollectionItem(collectionList[collectionName], rowList[i])

# Main program

if __name__ == '__main__':
    rowList = ReadDictCSV(dishFile)
    rowList = ToDishCollectionItem(rowList)
    InitCollection("Dish", rowList)

    rowList = ReadDictCSV(ingredientFile)
    InitCollection("Ingredient", rowList)

    rowList = ReadDictCSV(dishTypeFile)
    InitCollection("DishType", rowList)
