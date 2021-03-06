from config import *
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_admin.contrib.sqla import ModelView
from flask_admin import expose

#Data-Tables
customer_addresses = db.Table('customer_addresses', 
    db.Column('address_id', db.Integer, db.ForeignKey('address.id'), primary_key=True),
    db.Column('customer_id', db.Integer, db.ForeignKey('customer.id'), primary_key=True))

source_of_data_addresses = db.Table('source_of_data_addresses', 
    db.Column('address_id', db.Integer, db.ForeignKey('address.id'), primary_key=True),
    db.Column('source_of_data_id', db.Integer, db.ForeignKey('source_of_data.id'), primary_key=True))

#Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50), nullable = False, unique=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('Password is not readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __str__(self):
        return str(self.email)

#Prüfen Kombi aus beiden darf nur einmal vorkommen!
class UserAccess(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    source_of_data_id = db.Column(db.Integer, db.ForeignKey('source_of_data.id'))

    user = db.relationship('User', backref='users')
    source_of_data = db.relationship('Source_of_data', backref='source_of_datas')


class Source_of_data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False, unique=True)
    customer = db.relationship('Customer', backref='Source_of_data')
    invoices = db.relationship('Invoice', backref='Source_of_data')
    addresses = db.relationship('Address', backref='Source_of_data')
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, date_added):
        self.name = name
        self.date_added = date_added
     

    def __str__(self):
        return str(self.name)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_of_data_id = db.Column(db.Integer, db.ForeignKey('source_of_data.id'))
    street = db.Column(db.String(50), nullable = False)
    street_number = db.Column(db.String(15), nullable = False)
    postcode = db.Column(db.Integer, nullable = False)
    location = db.Column(db.String(30), nullable = False)
    date_added = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, id_source_of_data, street, street_number, postcode, location, date_added):
        self.source_of_data_id = id_source_of_data
        self.street = street
        self.street_number = street_number
        self.postcode = postcode
        self.location = location
        self.date_added = date_added

    def __str__(self):
        return str(self.street+' '+str(self.street_number)+', '+str(self.postcode)+' '+self.location)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_of_data_id = db.Column(db.Integer, db.ForeignKey('source_of_data.id'))
    name = db.Column(db.String(50), nullable = False)
    date_of_birth = db.Column(db.Date, nullable = False)
    telephone_number = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable = False)  
    invoices = db.relationship('Invoice', backref='customer')
    addresses = db.relationship('Address', secondary="customer_addresses", lazy='subquery', backref=db.backref('customer', lazy=True))
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, id_source_of_data,  name, date_of_birth, telephone_number, email, date_added):
        self.id_source_of_data = id_source_of_data
        self.name = name
        self.date_of_birth = date_of_birth
        self.telephone_number = telephone_number
        self.email = email
        self.date_added = date_added


    def __str__(self):
        return str(self.name)


class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_of_data_id = db.Column(db.Integer, db.ForeignKey('source_of_data.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    date = db.Column(db.Date, nullable = False)
    number = db.Column(db.String(30), nullable = False, unique=True)
    service = db.Column(db.String(50), nullable = False)
    amount = db.Numeric(10,2)
    created_at = db.Column(db.DateTime, default=datetime.now)
   
    def __init__(self, id_source_of_data, customer_id, date, number, service, amount, created_at):
        self.source_of_data_id = id_source_of_data
        self.customer_id = customer_id
        self.date = date
        self.number = number
        self.service = service
        self.amount = amount
        self.created_at = created_at


    def __str__(self):
        return str(self.number)
