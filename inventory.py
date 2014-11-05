# -*- coding: utf-8 -*-

import pymongo
from flask import Flask

inventory_app = Flask('InventoryApp')

client = pymongo.MongoClient("127.0.0.1", 27017)
db = client.inventory_app


@inventory_app.route('/offices_list')
def get_offices_list():
    offices = [office for office in db.offices.find()]
    return str(offices)
