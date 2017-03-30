#!/usr/bin/env python3.6
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
        self.conn = sqlite3.connect(os.path.join(os.getcwd(), 'krusty.db'))

    def close(self):
        """
        Stänger en förbindelse med databasen.
        """
        self.conn.close()

    def get_recipes(self):
        """
        Hämtar ingredienserna för alla produkter som finns i databasen.
        Returns:
            Returnerar en lista.
        """
        self.open()
        cursor = self.conn.execute('''
            SELECT r.productId, p.product, i.ingredient, r.quantity, r.unit
            FROM recipes AS r, products AS p, ingredients AS i
            WHERE r.productId = p.id AND r.ingredientId = i.id
        ''')
        self.close()
        return cursor
