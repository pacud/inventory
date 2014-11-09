# -*- coding: utf-8 -*-
from flask import render_template
from base import EndpointCollection


class Supplies(EndpointCollection):
    """Supplies related class"""

    def list(self):
        """Retrieves supplies and returns a list"""
        supplies = [supply for supply in self.db.supplies.find()]
        for supply in supplies:
            supply['quantity'] = int(supply['quantity'])
        return render_template('list_supplies.html', supplies=supplies)
