# -*- coding: utf-8 -*-

import pymongo
from flask import (
    Flask,
    render_template,
)
from offices import Offices
from supplies import Supplies

# init flask app
inventory_app = Flask('InventoryApp')

# init db
client = pymongo.MongoClient("127.0.0.1", 27017)
db = client.inventory_app

# init objects
office = Offices(db)
supplies = Supplies(db)


@inventory_app.route('/offices/list')
def get_offices_list():
    return office.list()


@inventory_app.route('/supplies/list')
def get_supplies_list():
    return supplies.list()


@inventory_app.route('/')
@inventory_app.route('/home')
def home():
    return render_template('home.html')
