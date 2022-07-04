from db_manager import DBManager
from pymongo.collection import Collection
from singleton import singleton


@singleton
class ReservationDao:
    dbManager = DBManager()
    collection = Collection(dbManager.db, 'Reservations')

    def insertReservation(self, reservationMap):
        self.dbManager.insert(self.collection, reservationMap)

    def findReservation(self, searchKeyValuePair):
        return self.dbManager.searchOne(self.collection, searchKeyValuePair)

    def editReservation(self, idToken, changedKeysValuesPairs):
        reservationInstanceMap = self.dbManager.readOne(self.collection, idToken)
        self.dbManager.update(self.collection, reservationInstanceMap, changedKeysValuesPairs)

    def deleteReservation(self, idToken):
        self.dbManager.delete(self.collection, idToken)
