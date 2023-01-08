import json

class Database():
    database = dict()
    pNameTable = dict()
    tagsTable = dict()

    def LoadDatabase(self):
        self.database = dict()
        f = open("stock.json", "r").read()
        self.database = json.loads(f)
        self.BuildIndexes()

    def BuildIndexes(self):
        self.pNameTable = dict()
        self.tagsTable = dict()
        #Iterate through each item
        for itemIndex in range(0, len(self.database["items"])):
            
            #Parse the title
            words = self.database["items"][itemIndex]["productName"].split(" ")
            for word in words:
                word = word.lower() #make lower case for uniformity

                if word in self.pNameTable: #If the word is already a key in the dict, append the index to key
                    self.pNameTable[word].append(itemIndex)
                else: #If it wasn't already a key, then make a new key and add item
                    self.pNameTable[word] = [itemIndex]
            
            #Load tags of item
            tags = self.database["items"][itemIndex]["tags"]

            #Add each tag to the tags index. this is the same idea as above
            for tag in tags:
                tag = tag.lower()
                if tag in self.tagsTable:
                    self.tagsTable[tag].append(itemIndex)
                else:
                    self.tagsTable[tag] = [itemIndex]
    
    def PerformSearch(self, query:str) -> list:
        sTermOccurences = [] #To store the indexes of the relevant items
        
        searchterms = query.split(" ")
        for searchterm in searchterms:
            #Remove any non-alphanumeric characters from the current search term
            searchterm = ''.join(c for c in searchterm if c.isalnum())

            #Check the product name index
            if searchterm in self.pNameTable:
                positions = self.pNameTable[searchterm]
                for position in positions:
                        sTermOccurences.append(position)
            
            #Check the tag index
            if searchterm in self.tagsTable:
                positions = self.tagsTable[searchterm]
                for position in positions:
                        sTermOccurences.append(position)
        
        #Sort the index occurences by the number of occurences, prioritising the most popular item
        prioritisedResults = sorted(sTermOccurences, key=lambda x: sTermOccurences.count(x), reverse=True)
        uniquePrioritisedResults = []

        duplicateOccurences = []
        for index in prioritisedResults:
            if uniquePrioritisedResults.count(index) != 0: continue
            uniquePrioritisedResults.append(index)
        
        return uniquePrioritisedResults
    
    def GetProduct(self, productNumber:str):
        item = None
        for i in range(0, len(self.database["items"])):
            if self.database["items"][i]["productNumber"] == productNumber:
                item = self.database["items"][i]
        
        return item

    def GetVariation(self, productNumber:str): #pNUm follows [xxx]:[y] format
        pNumComponents = productNumber.split(":")
        productNumber = pNumComponents[0]
        variantID = pNumComponents[1]
        
        variation = None
        item = self.GetProduct(productNumber)
        
        if item != None:
            for var in item["variations"]:
                if var["variantID"] == variantID:
                    variation = var
                    break
        
        return variation