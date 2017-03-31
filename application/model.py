from .database import Database


class Model(object):
    """
    Modellnivån.
    """
    def __init__(self):
        None

    def get_recipes(self):
        """
        Returnerar en lista med produkter och dess recept.
        Returns:    Lista med produkter och dess recept

        """
        return Database().get_recipes()
