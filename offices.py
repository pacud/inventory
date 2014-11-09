# -*- coding: utf-8 -*-
from base import EndpointCollection


class Offices(EndpointCollection):
    """Offices related class"""

    def list(self):
        """Retrieves offices and returns a list"""
        offices = [office for office in self.db.offices.find()]
        for office in offices:
            office['floor'] = int(office['floor'])
        return offices

    def defails(self, office_name):
        """Retrieves the repartition of a specific supply in offices"""
        crit = {'office': office_name}
        details = [detail for detail in self.db.diffusion.find(crit)]
        return details
