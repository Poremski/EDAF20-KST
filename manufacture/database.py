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

    def get_order_pall_list(self):
        self.open()
        cursor = self.conn.execute("SELECT DISTINCT po.'order', c.customer FROM product_orders AS po, orders AS o, customers AS c WHERE po.'order' = o.id AND o.customer = c.id AND po.quantity > (SELECT COUNT(p.product) FROM pallets AS p WHERE p.'order' = po.'order' AND p.product = po.product)")
        list = cursor.fetchall()
        self.close()
        return list

    def get_order_products(self, order):
        self.open()
        cursor = self.conn.execute("SELECT DISTINCT pr.product, po.quantity, (SELECT COUNT(p.product) FROM pallets AS p WHERE p.'order' = po.'order' AND p.product = po.product) FROM product_orders AS po, orders AS o, customers AS c, products AS pr WHERE po.'order' = o.id AND o.customer = c.id AND po.product = pr.id AND po.'order' = %s AND po.quantity > (SELECT COUNT(p.product) FROM pallets AS p WHERE p.'order' = po.'order' AND p.product = po.product)" % order)
        list = cursor.fetchall()
        self.close()
        return list

    def create_pallet(self, order, product):
        self.open()
        cursor = self.conn.execute("SELECT id FROM products WHERE product = '%s'" % (product, ))
        p = cursor.fetchall()
        p = [list(i)[0] for i in p][0]

        cursor = self.conn.execute("SELECT ingredientID, quantity, unit FROM recipes WHERE productId = %s" % (p, ))
        for ingredient in [list(i) for i in cursor.fetchall()]:
            self.update_raw_storage(ingredient[0], ingredient[1], ingredient[2])
        self.conn.execute("INSERT INTO pallets (product, 'order', location, blocked, created) VALUES(%s, %s, 'production', 0, DATE('now'))" % (p, order))
        self.conn.commit()
        self.close()
        return False

    def update_raw_storage(self, product, amount, unit):
        units = [
            ['kg', 1000],
            ['hg', 100],
            ['dag', 10],
            ['dg', 0.1],
            ['cg', 0.01],
            ['mg', 0.001],
            ['kL', 1000],
            ['hL', 100],
            ['daL', 10],
            ['dL', 0.1],
            ['cL', 0.01],
            ['mL', 0.001]
        ]

        q = amount*54

        for u in units:
            if u[0] is unit:
                q *= u[1]
                break

        self.conn.execute("UPDATE ingredients SET quantity = quantity-%s, last_delivered_quantity = %s, last_delivered_date = DATE('now') WHERE id = %s" % (q, q, product))
        self.conn.commit()

    def get_pallets(self):
        self.open()
        cursor = self.conn.execute("SELECT barcode FROM pallets")
        list = cursor.fetchall()
        self.close()
        return list

    def update_location(self, pallet, location):
        self.open()
        self.conn.execute("UPDATE pallets SET location = '%s' WHERE barcode = %s" % (location, pallet))
        self.conn.commit()
        self.close()
        return False