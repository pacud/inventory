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
    offices_list = office.list()
    return render_template('list_offices.html', offices=offices_list)


@inventory_app.route('/offices/details/<string:office_name>')
def get_office_details(office_name):
    details = office.defails(office_name)
    return render_template('details_offices.html', details=details)


@inventory_app.route('/supplies/list')
def get_supplies_list():
    supplies_list = supplies.list()
    return render_template('list_supplies.html', supplies=supplies_list)


@inventory_app.route('/supplies/details/<string:supply_name>')
def get_supply_details(supply_name):
    details = supplies.defails(supply_name)
    return render_template('details_supplies.html', details=details)


@inventory_app.route('/')
@inventory_app.route('/home')
def home():
    return render_template('home.html')
