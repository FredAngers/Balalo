from carte import Carte
from paquet import Paquet
from main import Main
import random as rad

# ante tuple : (level, power)
def Ante(level, boss, ante: tuple):
    anbe = "        ------------        \n" + f"        |  Ante {str(ante[0])}  |        \n"
    top = "----------------------------\n"
    sma = "|       Small Blind        |\n"
    bee = "|        Big Blind         |\n"
    boose = "|        Boss Blind        |\n"
    sboob = []
    for i in [1, 1.5, 2]:
        sboob += [ "|" + "       " + f"Score: {i * ante[1]}" + " " * (12 - (len(str(i * ante[1])))) + "|\n"]

    return anbe + top + sma + sboob[0] + top + bee + sboob[1] + top + boose + sboob[2] + top

def boss():
    pass

def menu():
    coici = input(
    "Type 'play' to fight the blind\n" +
    "Type 'deck' to view your deck and jokers\n" +
    "Type 'hands' to see the avilable hands and their power\n" +
    "Type 'boss' to view the effect of the boss blind\n" 
    )

    if coici not in ["play", "deck", "hands"]:
        coici = input(
            "not right word bish\n" +
            "Type 'play' to fight the blind\n" +
            "Type 'deck' to view your deck and jokers\n" +
            "Type 'hands' to see the avilable hands and their power\n" 
            )
    while coici in ["deck", "hands", "boss"]:
        if coici in ["deck"]:
            coici = input(f"{dic[daik]}\nWhat next?\n")
        elif coici in ["hands"]:
            coici = input(
                        f"{High}\n{High.description()}\n" +
                        f"{Pair}\n{Pair.description()}\n" +
                        f"{Two}\n{Two.description()}\n" +
                        f"{Three}\n{Three.description()}\n" +
                        f"{Straight}\n{Straight.description()}\n" +
                        f"{Flush}\n{Flush.description()}\n" +
                        f"{Full}\n{Full.description()}\n" + 
                        f"{Four}\n{Four.description()}\n" +
                        f"{Stgtfls}\n{Stgtfls.description()}\n" +
                        "What next?\n"
                        )
        elif coici in ["boss"]:
            pass
        return 'Lets a go mi amigo'
    
def round():
    pass



#maisn
High = Main("High card", 5, 1, "Play the highest card")
Pair = Main("Pair", 10, 2, "Play 2 of the same rank")
Two = Main("Two pair", 20, 2, "Play 2 pairs")
Three = Main("Three of a kind", 30, 3, "Play three of the same rank")
Straight = Main("Straight", 30, 4, "Play 5 cards, each with following rank")
Flush = Main("Flush", 35, 4, "Play 5 of the same suit")
Full = Main("Full house", 40, 4, "Play 2 of the same rank and 3 of the same rank")
Four = Main("Four of a kind", 60, 7, "Play 4 of the same rank")
Stgtfls = Main("Straight flush", 100, 8, "Play a straigt that is also a flush")

#paquey
normal = Paquet("normal")
pi = Paquet("pi")
sixy = Paquet("sixy", 4, 4)
dic = {
    "normal" : normal,
    "sixy" : sixy,
    "pi" : pi
}

print("------------\n" + "|  BALALA  |\n" + "------------\n\n" + "Type 'play' to start\n" + "Type 'bye' to close this\n")
choice = input("Your choice? : ")

#DECKCHOICECECECEC

if choice not in ["play", "bye"]:
    raise ConnectionRefusedError("Not the right word fucer")
elif choice in ["bye"]:
    raise RuntimeError("ok bye bye")



daik = input(f"Which deck will you choose ?\n{normal.dekipion()}{sixy.dekipion()}{pi.dekipion()}")
while daik not in ["normal", "pi", "sixy"]:
    daik = input(f"Not the right one\nWhich deck will you choose ?\n{normal.dekipion()}{sixy.dekipion()}{pi.dekipion()}")
    if daik in ["normal", "pi", "sixy"]:
        break

print(Ante(1, 4, (1, 300)))
print(menu())
