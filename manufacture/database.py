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

    def get_unblocked_pallets(self):
        self.open()
        cursor = self.conn.execute("SELECT barcode FROM pallets WHERE blocked = 0 AND location NOT IN ('delivering', 'delivered')")
        list = cursor.fetchall()
        self.close()
        return list

    def block_unblocked_pallet(self, pallet):
        self.open()
        self.conn.execute("UPDATE pallets SET blocked = 1 WHERE barcode = %s" % pallet)
        self.conn.commit()
        self.close()
        return False

    def unblock_blocked_pallet(self, pallet):
        self.open()
        self.conn.execute("UPDATE pallets SET blocked = 0 WHERE barcode = %s" % pallet)
        self.conn.commit()
        self.close()
        return False

    def get_order_list(self, chk_list):
        sql_blocked = ''
        if chk_list[0] is 1 and chk_list[1] is 1:
            pass
        elif chk_list[0] is 1 and chk_list[1] is 0:
            sql_blocked += ' AND blocked = 1'
        elif chk_list[0] is 0 and chk_list[1] is 1:
            sql_blocked += ' AND blocked = 0'
        else:
            sql_blocked += ' AND blocked is NULL'

        sql_location = '('
        if chk_list[2] is 1:
            sql_location += '\'production\','
        if chk_list[3] is 1:
            sql_location += '\'freezing\','
        if chk_list[4] is 1:
            sql_location += '\'packbags\','
        if chk_list[5] is 1:
            sql_location += '\'packbox\','
        if chk_list[6] is 1:
            sql_location += '\'loadpallet\','
        if chk_list[7] is 1:
            sql_location += '\'storage\','
        if chk_list[8] is 1:
            sql_location += '\'ramp\','
        if chk_list[9] is 1:
            sql_location += '\'delivering\','
        if chk_list[10] is 1:
            sql_location += '\'delivered\','

        if sql_location[-1] is ',':
            sql_location = sql_location[:-1]
        sql_location = ' AND location IN ' + sql_location + ')'

        self.open()
        cursor = self.conn.execute("SELECT o.id, c.customer, o.created, p.created, barcode, pr.product, location, blocked, delivery_date FROM orders AS o, customers AS c, product_orders AS po, pallets AS p, products AS pr WHERE o.customer = c.id AND o.id = po.'order' AND po.'order' = p.'order' AND po.product = pr.id AND po.product = p.product" + sql_blocked + sql_location)
        list = cursor.fetchall()
        self.close()
        return list