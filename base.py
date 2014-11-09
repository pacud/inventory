# -*- coding: utf-8 -*-


class EndpointCollection(object):
    """Basic class for endpoints collection"""

    def __init__(self, db_client):
        """initialises a collection

        :param db_client: mongo client
        """
        self.db = db_client
