from . import configurations


class Model:
    """
    Modellen:   Klassen innehåller datastrukturen.
                -- Kontrollern kan skicka meddelanden till Modellen
                   och Modellen kan besvara dem.
                -- Modellen använder delegater för att sända meddelanden
                   till Kontrollern vid förändring.
                -- Modellen kommunicerar ALDRIG med Vyn.
                -- Modellen har getters och setters för att kommunicera
                   med Kontrollern.
    """
    def __init__(self, vc):
        self.vc = vc
