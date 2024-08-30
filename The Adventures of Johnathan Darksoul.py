# The Adventures of Johnathan Darksoul
import random
attdecision = "self.strength"
class Johndarksoul:
    def __init__(self, strength, dexterity, vigor, luck, faith, intelligence):
        self.strength = strength
        self.dexterity = dexterity
        self.vigor = vigor
        self.luck = luck
        self.faith = faith
        self.intelligence = intelligence
        self.stats(self.strength, self.dexterity, self.vigor, self.luck, self.faith, self.intelligence)

        def levelup():
            for i in self.stats:
                if str(i) == attdecision:
                    i = i + 1
jds = Johndarksoul(1,1,1,1,1,1)
levelup()