from bson import ObjectId
from flask import Flask, request
from flask_pymongo import PyMongo
import bson.json_util as json
import customer_dao
import reservation_dao


app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://127.0.0.1:27017/gestionale2022_2'
mongo = PyMongo(app)

########################################################################
###############################CUSTOMERS VIEWS##########################
########################################################################

customerDao = customer_dao.CustomerDao()

@app.route('/api/customers')
def customers():
    cursor = mongo.db.Customers.find()
    elements = []
    for document in cursor:
        elements.append(document)
    return json.dumps(elements)
    #parsed = json.load(elements)
    # return json.dumps(parsed , indent=4, sort_keys=True)


@app.route('/api/getCustomer/')
def getCustomer(methods = 'GET'):
    field = request.args.get('field')
    value = request.args.get('value')
    elements = []
    cursor = customerDao.findCustomer({field: value})
    for document in cursor:
        elements.append(document)
    return json.dumps(str(elements))

@app.route('/api/modifyCustomer')
def modifyCustomer(methods = ['GET', 'POST']):
    stringId = request.args.get('stringId')
    field = request.args.get('field')
    value = request.args.get('value')
    objInstance = ObjectId(stringId)
    map = {field: value}
    customerDao.editCustomer(objInstance, map)
    return 'customer modified'
    #esempio: http://127.0.0.1:5000/api/modifyCustomer?stringId=6287c74fd353b9d062d7f719&field=name&value=michele

@app.route('/api/newCustomer')
def newCustomer(methods = ['POST']):
    name = request.args.get('name')
    surname= request.args.get('surname')
    email= request.args.get('email')
    phoneNumber= request.args.get('phoneNumber')
    map = {
        'name' : name,
        'surname' : surname,
        'email' : email,
        'phoneNumber' : phoneNumber
    }
    customerDao.insertCustomer(map)
    return 'customer added'
    #esempio: http://127.0.0.1:5000/api/newCustomer?name=carlo&surname=olrac&email=carlo@carlo.carlo&phoneNumber=3499494449

@app.route('/api/deleteCustomer')
def deleteCustomer(methods = ['DELETE']):
    stringId = request.args.get('stringId')
    objInstance = ObjectId(stringId)
    customerDao.deleteCustomer(objInstance)
    return 'customer deleted'



########################################################################
###############################RESERVATION VIEWS########################
########################################################################

reservationDao = reservation_dao.ReservationDao()

@app.route('/api/reservations')
def reservations():
    cursor = mongo.db.Reservations.find()
    elements = []
    for document in cursor:
        elements.append(document)
    return json.dumps(str(elements))


@app.route('/api/getReservation')
def getReservation(methods = 'GET'):
    field = request.args.get('field')
    value = request.args.get('value')
    elements = []
    cursor = reservationDao.findReservation({field: value})
    for document in cursor:
        elements.append(document)
    return json.dumps(str(elements))


@app.route('/api/modifyReservation')
def modifyReservation(methods = ['GET', 'POST']):
    stringId = request.args.get('stringId')
    field = request.args.get('field')
    value = request.args.get('value')
    objInstance = ObjectId(stringId)
    map = {field: value}
    reservationDao.editReservation(objInstance, map)
    return 'reservation modified'

@app.route('/api/newReservation')
def newReservation(methods = ['POST']):
    customerId = request.args.get('customerId')
    discount = request.args.get('discount')
    beachChairs= request.args.get('beachChairs')
    beachBundle= request.args.get('beachBundle')
    date= request.args.get('date')
    daySlot= request.args.get('daySlot')
    tickets= request.args.get('tickets')
    totalCost= request.args.get('totalCost')

    map = {
      'customerId': customerId,
      'discount': discount,
      'beachChairs': beachChairs,
      'beachBundle' : beachBundle,
      'date': date,
      'daySlot': daySlot,
      'tickets': tickets,
      'totalCost': totalCost,
    }
    reservationDao.insertReservation(map)
    return 'reservation added'



@app.route('/api/deleteReservation')
def deleteReservation(methods = ['DELETE']):
    stringId = request.args.get('stringId')
    objInstance = ObjectId(stringId)
    reservationDao.deleteReservation(objInstance)
    return 'reservation deleted'


########################################################################
###############################APP+DB SETUP##########################
########################################################################
if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=5000, ssl_context='adhoc')



