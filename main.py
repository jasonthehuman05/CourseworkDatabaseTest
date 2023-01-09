import tkinter
import json
import dbase
import ItemCreator

db = dbase.Database()
db.LoadDatabase() 

nItem = ItemCreator.CreateItem()
db.AddToDatabase(nItem)
print(db.database["items"][3]["productName"])
db.WriteDatabase()