class Category:
    def __init__(self,name,totalAmount):
        self.name = name
        self.totalAmount = totalAmount

    def getAmountSpent(self):
        return self.totalAmount
    
    def modifyCategoryName(self,newName):
        self.name = newName

