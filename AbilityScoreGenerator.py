import random as r
def abilityS():
    aScores = {"Strenght": [], "Dexterity": [], "Constitution": [], "Intelligence": [], "Wisdom": [], "Charisma": []}

    for i in aScores:
        roll = []
        for x in range(4):
            roll.append(r.randint(1,6))
        roll.remove(min(roll))
        aScores[i] = [sum(roll)]
        print(i, aScores[i])
    #restarts program upon request
    Again = input("try again? (Y or N)")
    if Again == "Y" or Again == "y":
        print()
        abilityS()

abilityS()        
