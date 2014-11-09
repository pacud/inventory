# -*- coding: utf-8 -*-
from base import EndpointCollection


class Supplies(EndpointCollection):
    """Supplies related class"""

    def list(self):
        """Retrieves supplies and returns a list"""
        supplies = [supply for supply in self.db.supplies.find()]
        for supply in supplies:
            supply['quantity'] = int(supply['available_quantity'])
        return supplies

    def defails(self, supply_name):
        """Retrieves the repartition of a specific supply in offices"""
        crit = {'supply': supply_name}
        details = [detail for detail in self.db.diffusion.find(crit)]
        return details
