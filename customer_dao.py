from db_manager import DBManager
from pymongo.collection import Collection
from singleton import singleton

@singleton
class CustomerDao:
    dbManager = DBManager()
    collection = Collection(dbManager.db, 'Customers')

    def showCustomers(self):
        return self.dbManager.readAll('Customers')

    def insertCustomer(self, customerMap):
        self.dbManager.insert(self.collection, customerMap)

    def findCustomer(self, searchKeyValuePair):
        return self.dbManager.searchOne(self.collection, searchKeyValuePair)

    def editCustomer(self, ObjectId, changedKeysValuesPairs):
        # customerInstanceMap = self.dbManager.readOne(self.collection, idToken)
        searchId = {'_id' : ObjectId}
        self.dbManager.update(self.collection, searchId, changedKeysValuesPairs)

    def deleteCustomer(self, idToken):
        self.dbManager.delete(self.collection, idToken)



