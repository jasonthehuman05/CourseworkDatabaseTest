import tkinter
import json
import dbase

db = dbase.Database()
db.LoadDatabase() 

variation = db.GetVariation(input("Enter product number\n>>> "))

print(variation["variationName"])