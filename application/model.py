#!/usr/bin/env python3
from .database import Database


class Model(object):
    """
    Modellnivån.
    """
    def __init__(self):
        self.db = Database()

    def get_recipes(self):
        """
        Returnerar en lista med produkter och dess recept.
        Returns:    Lista med produkter och dess recept.

        """
        return self.db.get_recipes()

    def get_products(self):
        """
        Returnerar en dict med id-nummer som nycke och produktnamn som värde.
        Returns:    Dict innehållandes produkter.
        """
        products = self.db.get_products()
        list = dict()
        for product in products:
            list[product[0]] = product[1]
        return list

    def get_units(self):
        """
        Returnerar en dict med enhet som nycke och enhetsnamn som värde.
        Returns:    Dict innehållandes produkter.
        """
        units = self.db.get_units()
        list = dict()
        for unit in units:
            list[unit[0]] = unit[1]
        return list

    def get_ingredients(self):
        """
        Returnerar en dict med id-nummer som nycke och ingrediensnamn som värde.
        Returns:    Dict innehållandes produkter.
        """
        ingredients = self.db.get_ingredients()
        list = dict()
        for ingredient in ingredients:
            list[ingredient[0]] = ingredient[1]
        return list
