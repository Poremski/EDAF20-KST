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

    def get_blocked_pallets(self):
        self.open()
        cursor = self.conn.execute("SELECT barcode FROM pallets WHERE blocked = 1")
        list = cursor.fetchall()
        self.close()
        return list

    def get_order_list(self):
        self.open()
        cursor = self.conn.execute("SELECT o.id, c.customer, o.created, p.created, barcode, pr.product, location, blocked, delivery_date FROM orders AS o, customers AS c, product_orders AS po, pallets AS p, products AS pr WHERE o.customer = c.id AND o.id = po.'order' AND po.'order' = p.'order' AND po.product = pr.id AND po.product = p.product")
        list = cursor.fetchall()
        self.close()
        return list