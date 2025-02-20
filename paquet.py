from carte import Carte

class Paquet(Carte):
    def __init__(self, type, slots=10, hand=8, deek=None, dekip="po"):
        self.deek = deek if deek is not None else []
        self.type = type
        self.slots = slots
        self.hand = hand
        self.dekip = dekip
        self.construire_le_paquet()

    def __str__(self):
        return f"Deck type : {self.type}\n" + f"Hand size: {self.hand}\n" + f"Joker slots : {self.slots}\n" + f"{self.deek}\n"
    
    def construire_le_paquet(self):
        if self.type not in ["normal", "sixy", "pi"]:
            raise TypeError("Wrong type of deck")
        else:
            if self.type in ["normal", "sixy"]:
                for i in ["clubs", "diamonds", "hearts", "spades"]:
                    for g in [2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace"]:
                        if self.type == "normal":
                            self.deek.append(Carte(g, i, None))
                        elif self.type == "sixy":
                            self.deek.append(Carte(6, i, None))
            if self.type == "pi":
                for i in ["clubs", "diamonds", "hearts", "spades"]:
                    for g in [3, "ace", 4, "ace", 5, 9, 2, 6, 5, 3, 5, 8, 9]:
                        self.deek += [Carte(g, i, None)]
        return self.deek

    def paquet_modif(self, modi: Carte, ajou=True):
        if ajou is True:
            self.deek.append(modi)
        else:
            if modi not in self.deek:
                raise TypeError("Card not in deck.")
            else:
                self.deek.remove(modi)
        return self.deek
    
    def dekipion(self):
        if self.type not in ["normal", "sixy", "pi"]:
            raise TypeError("Wrong type of deck")
        if self.type in ["normal"]:
            return "normal : 13 cards per suit (boring)\n8 hand size, 10 joker slots\n"
        elif self.type in ["sixy"]:
            return "sixy : Me likee sixee\n4 hand size, 4 joker slots\n"
        elif self.type in ["pi"]:
            return "pi : 3.141592653589\n7 hand size, 9 joker slots\n"
