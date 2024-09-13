class Mortal:
    def __init__(self, strength, dexterity, vigor, luck, faith, intelligence):
        self.strength = strength
        self.dexterity = dexterity
        self.vigor = vigor
        self.luck = luck
        self.faith = faith
        self.intelligence = intelligence
class Meathead(Mortal):
    def __init__(self, stamina, armor, strength, dexterity, vigor, luck, faith, intelligence):
        super().__init__(strength, dexterity, vigor, luck, faith, intelligence)
        self.stamina = stamina
        self.armor = armor
class Wisened(Mortal):
    def __init__(self, mana, maxmana, strength, dexterity, vigor, luck, faith, intelligence):
        super().__init__(strength, dexterity, vigor, luck, faith, intelligence)
        self.mana = mana
        self.maxmana = maxmana
class Vagabond(Mortal):
    def __init__(self, agility, lethality, strength, dexterity, vigor, luck, faith, intelligence):
        self.agility = agility
        self.lethality = lethality
        super().__init__(strength, dexterity, vigor, luck, faith, intelligence)
class Godling(Mortal):
    def __init__(self, charisma, reverence, strength, dexterity, vigor, luck, faith, intelligence):
        super().__init__(strength, dexterity, vigor, luck, faith, intelligence)
        self.charisma = charisma
        self.reverence = reverence
class Wretch(Mortal):
    def __init__(self):
        self.strength = 0
        self.dexterity = 0
        self.vigor = 0
        self.luck = 0
        self.faith = 0
        self.intelligence = 0

print(" You are currently Ninety Nine Below. All you have known has been consumed by the Crumble,\n a result of a ritual to crack the Earth and bring forth Hell. The occultists,\n well versed in manipulating fate, hid their lair from the very gods beneath the Earth.\n Now that you're underground, too, you ought to find them before the demons get you.\n You remember you were...")
print("...a mortal...\n...a wretched beast...")
choice = input()

def choice1():
    global choice, result, player
    if choice == "a mortal":
        result = 1
        print("I remember a little more... You were Man, a creature of war and industry. \nYour industry happened to be mercenary work...")
        choice = input("...a hireling...\n...a battlemage...\n...a picklock...\n...a priest...")
    elif choice == "a wretched beast":
        result = 0
        print(" I remember a little more... You were a Wretch, the lowliest of Daemons. You are a doomed creature. \n The journey that awaits you was never for you to take, but, if you prove worthy, you will\n recieve it's reward all the same. I cannot lie to you; I am not rooting for you in the slightest.")
        player = Wretch()
    else:
        print("No, you were not. What were you, truly..?")
        print("...a mortal...\n...a wretched beast...")
        choice = input()
        choice1()
def choice2():
    global choice, result, player
    if choice == "a hireling":
        print("You could wield a sword, axe, or spear just fine, and it suited your explosive personality.\n You have lived in the Channel for ages; you've almost grown accustomed to the sound of the Underriver and the bodies that happen to fall in.\n Slaying some hellspawn will be a piece of cake for you.")
        player = Meathead(0,0,5,2,2,2,2,2)
    elif choice == "a battlemage":
        print("You were born gifted with magicks. Thankfully, you weren't put to death immediately after you were found.\n No, the King prefered a delayed death, one where he could use you. The Fields of War.\n You were fighting the army Rathuko, the Ancient Dragon sent to quell your tax rebellion before you fell into the pits of Hell.\n Obliterating these demons and their summoners will be a piece of cake for a mage like you.")
        player = Wisened(0,0,2,2,2,2,2,5)
    elif choice == "a picklock":
        print("You fell in with the unsavory folk at the beginning of your life. You learnt quickly, and you were put to use.\n You began life as a dungeon raider, an almost legal profession.\n Unfortunately, the Dungeon was the first to go when the Crumbling came.\n Evading these daemons will be a piece of cake. You might even kill a few.")
        player = Vagabond(0,0,2,5,2,2,2,2)
    elif choice == "a priest":
        print("You actually jumped into the Crumble willingly, you damnable fool.\nNo matter- you wanted this, after all. With talk of daemons rising to the Earth, you just\nHAD to jump in and quell the Unholy Army. Alone. I hope you have a plan.\n This will not be a piece of cake.")
        player = Godling(0,0,2,2,2,2,5,2)
    else:
        print("No, you were not. What were you, truly..?")
        choice = input("...a hireling...\n...a battlemage...\n...a picklock...\n...a priest...")
def introduction():
    print("You open your eyes. Bruised and battered from the roughly hundred foot drop,\n you barely manage to pick yourself up. A doorway lies between you and your journey. It is locked.\n")


choice1()
choice2()
introduction()