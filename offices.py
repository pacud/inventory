# -*- coding: utf-8 -*-
from flask import render_template
from base import EndpointCollection


class Offices(EndpointCollection):
    """Offices related class"""

    def list(self):
        """Retrieves offices and returns a list"""
        offices = [office for office in self.db.offices.find()]
        for office in offices:
            office['floor'] = int(office['floor'])
        return render_template('list_offices.html', offices=offices)
