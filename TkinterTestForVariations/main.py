import tkinter
import json

def passer():
    pass

class RootWindow:
    def __init__(self, title):
        self.root = tkinter.Tk()
        self.root.withdraw()
        self.DisplayLoginWindow()
        self.root.mainloop()
    def DisplayLoginWindow(self):
        loginWindow = ItemWindow(self.root)

# class LoginWindow():
#     def __init__(self, rootWindow):
#         self.root = tkinter.Toplevel()
#         self.root.geometry("300x200")
#         self.root.title("Log in to BuildrightDB")
#         self.rootWindow = rootWindow
#         self.CreateWidgets()
#         self.root.protocol("WM_DELETE_WINDOW", lambda: passer())
#     def CreateWidgets(self):
#         titleLabel = tkinter.Label(self.root, text="Log In")
#         titleLabel.pack()
#         quitButton = tkinter.Button(self.root, text="Log In", command=lambda:self.rootWindow.destroy())
#         quitButton.pack()
#         quitButton = tkinter.Button(self.root, text="Quit", command=lambda:self.rootWindow.destroy())
#         quitButton.pack()

class ItemWindow():
    def __init__(self, rootWindow):
        self.root = tkinter.Toplevel()
        self.root.geometry("300x200")
        self.root.title("ItemInformationWindowTitle")
        self.rootWindow = rootWindow
        #self.root.protocol("WM_DELETE_WINDOW", lambda: passer())
        self.LoadJson()
    
    def LoadJson(self):
        f = open("TkinterTestForVariations/itemInformation.json", "r").read()

        data = json.loads(f)
        item = data['items'][0]
        print(f"----{item['itemName']}----")
        print(f"VARIATIONS: {item['itemVariations']['variationName']}")
        for variation in item["itemVariations"]["variationTypes"]:
            print(variation["variationName"], " === ", variation["variationCost"])

        

window = RootWindow("Hewrfojuhwipefo")