def CreateItem():
    prodNum = str(input("Enter Product Number\n>>"))
    prodName = str(input("Enter product name\n>>"))
    tags = []
    while True:
        inp = input("Enter another tag, or enter ### to finish\n>>")
        if inp == "###": break
        else:
            tags.append(inp)

    variations = []
    while True:
        vID = str(input("Enter variant ID, or enter ### to finish.\n>>"))
        if vID == "###": break
        else:
            vName = str(input("Enter variant name\n>>"))
            vCost = float(input("Enter variant cost\n>> £"))
            variation = {
                "variantID": vID,
                "variationName": vName,
                "variationCost": vCost
            }

    newItem = {
            "productNumber": prodNum,
            "productName": prodName,
            "tags": tags,
            "variations": variations
    }
    return newItem