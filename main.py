class Main:
    def __init__(self, nom, chip, mult, desc="booboo", level=1):
        self.chip = chip
        self.mult = mult
        self.level = level
        self.nom = nom
        self.desc = desc

    def __str__(self):
        return f"{self.nom} level {self.level} : {self.chip} x {self.mult}"
    
    def level_up(self, num=1):
        self.level += num
        return self.level
    
    def description(self):
        return self.desc