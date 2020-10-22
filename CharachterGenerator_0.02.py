import random as r
#for rand
def abilityS():
    aScores = {"Strength": [], "Dexterity": [], "Constitution": [], "Intelligence": [], "Wisdom": [], "Charisma": []}

    print('Ability Scores \n')    
    for i in aScores:
        roll = []
        for x in range(4):
            roll.append(r.randint(1,6))
        roll.remove(min(roll))
        aScores[i] = [sum(roll)]
        print(i, aScores[i])
#for class
##def ability():
##        roll = []
##        for x in range(4):
##            roll.append(r.randint(1,6))
##        roll.remove(min(roll))
##        return (sum(roll))
def aligngen():
    GE = ['Good', 'Neutral', 'Evil']
    LC = ['lawfull ', 'Neutral ', 'Chaotic ']
    roll1 = r.randint(0, 2)
    roll2 = r.randint(0, 2)
    return(LC[roll2] + GE[roll1])

def Backggen():

    Background = ['Acolyte','Anthropologist','Charlatan','City Watch','Clan Crafter','Cloistered Scholar','Criminal','Dissenter','Entertainer','Faction Agent','Far Traveler','Folk Hero','Guild Artisan','Haunted One','Hermit','House Agent','Inheritor','Initiate','Inquisitor','Investigator','Knight Of The Order','Mercenary Veteran','Noble','Outlander','Sage','Sailor','Soldier','Urban Bounty Hunter','Urchin','Tribe Member','Vizier']    
    roll = r.randint(0, 30)
    return(Background[roll])

def classgen():
    
    Class = ['Artificer','Barbarian','Bard','Blood Hunter','Cleric','Druid','Fighter','Monk','Mystic','Paladin','Ranger','Rogue','Sorcerer','Warlock','Wizard']
    roll = r.randint(0, 14)
    return(Class[roll])

def racegen():
    race = ['Arakora', 'Aasimar', 'Aetherborn', 'Aven', 'Bugbear', 'Centaur', 'Changeling', 'Dragonborn', 'Drow', 'Dwarf', 'Elf', 'Firbolg', 'Genasi', 'Gith', 'Gnome', 'Goblin', 'Goliath', 'Half-Elf', 'Halfling', 'Half-Ork', 'Hobgoblin', 'Human', 'Kalashtar', 'Kenku', 'Khenra', 'Kobold', 'Kor', 'Lizardfolk', 'Loxodon', 'Merfolk', 'Minotaur', 'Naga', 'Ork', 'Shifter', 'Simic Hybrid', 'Tabaxi', 'Tiefling', 'Tortle', 'Triton', 'Vampire', 'Vedalken', 'Viashino', 'Worforged', 'Yan-ti Pureblood']
    
    roll = r.randint(0, 43)
    return(race[roll])
def RNameGenerator():
    name = ''
    vowel = ['a','e','i','o','u','y']
    consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','qu',
                 'r','s','t','u','v','w','x','z',"'",'-']
    length = r.randint(1, 7)
    if length == 1:
        name = vowel[r.randint(0,5)]
    else:
        for x in range(length):
            VorC = r.randint(1,2)
            if VorC == 1:
                name += vowel[r.randint(0,5)]
            else:
                name += consonant[r.randint(0,21)]
                
    return(name.capitalize())

class Character:
    def __init__(self):
        self.name = RNameGenerator()
        self.Alignment = aligngen()
        self.Class = classgen ()
        self.Background = Backggen()
        self.Strength = self.ability()
        self.Dexterity = self.ability()
        self.Constitution = self.ability()
        self.Intelligence = self.ability()
        self.Wisdom = self.ability()
        self.Charisma = self.ability()
    def ability(self):
        roll = []
        for x in range(4):
            roll.append(r.randint(1,6))
        roll.remove(min(roll))
        return (sum(roll))
    
        
        
        
def charachtergen():
    print('\n')
    print('Your charachter is', RNameGenerator())
    print("a", aligngen())
    print(racegen(),',', classgen())
    print('that is a', Backggen())
    print('')
    abilityS()
    
    #restarts program upon request:
    print()
    Again = input("try again? \n(Y or N)")
    if Again == "Y" or Again == "y":
        print()
        charachtergen()

charachtergen()

