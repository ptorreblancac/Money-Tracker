class Dashboard:
    def __init__(self):
        self.transactionList = [] #includes a list of all transaction objects
        self.categoryList = []
        
    def getAllTransactions(self):
        return self.transactionList
    
    def addTransaction(self,t):
        self.transactionList.append(t)

    def getAllCategories(self):
        return self.categoryList
    
    def addCategory(self,c):
        self.categoryList.append(c)
    
    def removeCategory(self,cat):
        self.categoryList.remove(cat)

    def updateCategories(self,i,newName):
        self.categoryList[i].name = newName

    def findCategory(self,nameCat):
        for c in self.categoryList:
            if (c.name == nameCat):
                return True
        return False


        

        
    
            
