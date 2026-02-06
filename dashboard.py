from category import Category

class Dashboard:
    def __init__(self):
        self.transactionList = [] #includes a list of all transaction objects
        self.categoryList = []
        
    def getAllTransactions(self):
        return self.transactionList
    
    def getTransaction(self,i):
        return self.transactionList[i]
    
    def editTransaction(self,opt,newValue,fieldName):
        setattr(self.transactionList[opt],fieldName,newValue)
        
    
    def addTransaction(self,t):
        categoryExisted = self.findCategory(t.category)
        if (not categoryExisted): # verify if category existed already, if not add it
            if (t.type == 'expense'): # substract expenses from total amount
                amount *= -1
            c = Category(t.category,t.amount)
            self.addCategory(c) # add the category to the list

        self.transactionList.append(t) # add the transaction to the list

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


        

        
    
            
