import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Food(db.Model):
    __tablename__ = 'foods'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, unique=True, nullable=False)
    auto_buy = db.Column(db.Boolean, nullable=False, default=False)


    def __init__(self, name: str, auto_buy: str):
        self.name = name
        self.auto_buy = auto_buy

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "auto_buy": self.auto_buy
        }

class ShoppingList(db.Model):
    __tablename__ = 'shopping_list'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    food_id = db.Column(db.Integer, db.ForeignKey('foods.id'), unique=True, nullable=False)
    num_units = db.Column(db.Integer, default=1)
    date_added = db.Column(db.Date, nullable=False)

    def __init__(self, food_id: int, num_units: int, date_added: datetime):
        self.food_id = food_id
        self.num_units = num_units
        self.date_added = date_added

    def serialize(self):
        return {
            'id': self.id,
            'food_id': self.food_id,
            'date_added': self.date_added.isoformat(),
            'num_units': self.num_units
        }

class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location_name = db.Column(db.Text, unique=True, nullable=False)

    def __init__(self, location_name: str):
        self.location_name = location_name

    def serialize(self):
        return {
            'id': self.id,
            'location_name': self.location_name
        }

class ShoppingTrip(db.Model):
    __tablename__ = 'shopping_trips'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __init__(self, location_id: id, date: datetime):
        self.location_id = location_id
        self.date = date

    def serialize(self):
        return {
            'id': self.id,
            'location_id': self.location_id,
            'date': self.date.isoformat()
        }

class ShoppingTripItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    shopping_trip_id = db.Column(db.Integer, db.ForeignKey('shopping_trips.id'), nullable=False)
    food_id = db.Column(db.Integer, db.ForeignKey('foods.id'), nullable=False)
    price = db.Column(db.Float, default = 0.00, nullable = False)

    def __init__(self, shopping_trip_id: id, food_id: id, price: float):
        self.shopping_trip_id = shopping_trip_id
        self.food_id = food_id
        self.price = price

    def serialize(self):
        return {
            'id': self.id,
            'shopping_trip_id': self.shopping_trip_id,
            'food_id': self.food_id,
            'price': self.price
        }

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    food_id = db.Column(db.Integer, db.ForeignKey('foods.id'), nullable=False)
    shopping_trip_item_id = db.Column(db.Integer, db.ForeignKey('shopping_trip_items.id'), nullable=False)
    in_stock = db.Column(db.Boolean, nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)
    
    def __init__(self, food_id: id, shopping_trip_item_id: id, in_stock: bool, expiration_date: datetime):
        self.food_id = food_id
        self.shopping_trip_item_id = shopping_trip_item_id
        self.in_stock = in_stock
        self.expiration_date = expiration_date

    def serialize(self):
        return {
            'id': self.id,
            'food_id': self.food_id,
            'shopping_trip_item_id': self.shopping_trip_item_id,
            'in_stock': self.in_stock,
            'expiration_date': self.expiration_date
        }