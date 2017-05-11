#!/usr/bin/env python3
import os
import sqlite3


class Database(object):
    """
    Databashanterare som sköter all kommunikation med databasen.
    """

    def __init__(self):
        """
        Konstruktorn för databashanteraren.
        """
        self.conn = None

    def open(self):
        """
        Öppnar en förbindelse med databasen.
        """
        self.conn = sqlite3.connect(os.path.join(os.getcwd(), '../krusty.db'))

    def close(self):
        """
        Stänger en förbindelse med databasen.
        """
        self.conn.close()

    def set_new_user(self, customer, address, country):
        """
        Lägg till en ny användare i databasen.
        Args:
            customer:   Anger företagsnamnet
            address:    Anger kundens adress.
            country:    Anger adressens land.

        Returns:    Returnerar True om kunden lades till i databasen, annars False.
        """
        self.open()
        t = (customer, address, country)
        self.conn.execute("INSERT INTO customers (customer, address, country) VALUES ('%s', '%s', '%s')" % t)
        self.conn.commit()
        self.close()
        return False
