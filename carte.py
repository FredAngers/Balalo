class Carte:
    def __init__(self, rank, suit, enhan=None):
        self.rank = rank
        self.suit = suit
        self.enhan = enhan

    def __str__(self):
        if self.suit not in ["clubs", "spades", "hearts", "diamonds"]:
            raise TypeError("Wrong format of suit.")
        elif self.rank not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace"]:
            raise TypeError("Wrong format of rank.")
        else:
            if self.enhan is None:
                return f"{self.rank} of {self.suit}"
            else:
                return f"{self.enhan} {self.rank} of {self.suit}"
    
    def __repr__(self):
        if self.suit not in ["clubs", "spades", "hearts", "diamonds"]:
            raise TypeError("Wrong format of suit.")
        elif self.rank not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace"]:
            raise TypeError("Wrong format of rank.")
        else:
            if self.enhan is None:
                return f"{self.rank} of {self.suit}"
            else:
                return f"{self.enhan} {self.rank} of {self.suit}"
    
    def __eq__(self, other):
        if isinstance(other, Carte):
            return self.rank == other.rank and self.suit == other.suit
        return False