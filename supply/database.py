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

    def get_recipes(self):
        """
        Hämtar ingredienserna för alla produkter som finns i databasen.
        Returnerar:
            Returnerar en lista.
        """
        self.open()
        cursor = self.conn.execute('''
            SELECT r.productId, p.product, i.ingredient, r.quantity, r.unit
            FROM recipes AS r, products AS p, ingredients AS i
            WHERE r.productId = p.id AND r.ingredientId = i.id
        ''')
        list = cursor.fetchall()
        self.close()
        return list

    def set_recipes(self, product_id, ingredient_id, quantity, unit):
        """
        Lägger till ingrediens till en produkt.
        Returnerar:
            Returnerar en lista.
        """
        self.open()
        t = (product_id, ingredient_id, quantity, unit)
        self.conn.execute("INSERT INTO recipes VALUES (?, ?, ?, ?)" % t)
        self.conn.commit()
        self.close()
        return list

    def get_products(self):
        """
        Hämtar alla produkter som finns i databasen.
        Returnerar:
            Returnerar en lista.
        """
        self.open()
        cursor = self.conn.execute("SELECT id, product FROM products")
        list = cursor.fetchall()
        self.close()
        return list

    def set_product(self, product_name):
        """
        Skapar en ny produkt i databasen.
        Args:
            product_name:   Anger namnet på produkten

        Returns:    Returnerar True om produkten skapades, annars False.
        """
        self.open()
        t = (product_name, )
        cursor = self.conn.execute("INSERT INTO products (product) VALUES ('?')" % t)
        c = self.conn.commit()
        self.close()
        return False

    def del_product(self, product_id):
        """
        Tar bort en produkt i databasen.
        Args:
            product_id:   Anger id på det produkt som ska tas bort.

        Returns:    Returnerar True om produkten har blivit borttagen, annars False.
        """
        self.open()
        t = (product_id, )
        self.conn.execute("DELETE FROM products WHERE id = ?" % t)
        self.conn.execute("DELETE FROM recipes WHERE productId = ?" % t)
        self.conn.commit()
        self.close()
        return False

    def get_ingredients(self):
        """
        Hämtar alla ingredienser som finns i databasen.
        Returnerar:
            Returnerar en lista.
        """
        self.open()
        cursor = self.conn.execute("SELECT id, ingredient FROM ingredients")
        list = cursor.fetchall()
        self.close()
        return list

    def set_ingredients(self,ingredient_name):
        """
        Lägger in en ingrediens i databasen.
        Args:
            ingredient_name:    Namnet på den ingrediens som ska läggas in i databasen.

        Returns:    Returnerar True om ingrediensen lades till, annars False.

        """
        self.open()
        t = (ingredient_name, )
        self.conn.execute("INSERT INTO ingredients (ingredient) VALUES ('?')" % t)
        self.conn.commit()
        self.close()
        return False

    def del_ingredients(self,ingredient_id):
        """
        Tar bort en ingrediens från database.
        Args:
            ingredient_id: Ingrediensens ID-nummer som ska tas bort.

        Returns: Returnerar True om ingrediensen togs bort, annars False.

        """
        self.open()
        t = (ingredient_id, )
        self.conn.execute("DELETE FROM ingredients WHERE id = ?" % t)
        self.conn.execute("DELETE FROM recipes WHERE ingredientId = ?" % t)
        self.close()
        return False

    def get_units(self):
        """
        Hämtar alla enheter som finns i databasen.
        Returnerar:
            Returnerar en lista.
        """
        self.open()
        cursor = self.conn.execute("SELECT unit, name FROM units")
        list = cursor.fetchall()
        self.close()
        return list
