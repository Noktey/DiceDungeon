class Personnage:
    def __init__(self, name, hp_max, dice):
        self.name = name
        self.hp_max = hp_max
        self.hp = hp_max
        self.dice = dice

    def getHPPerso(self):
        return self.hp

    def getHPMaxPerso(self):
        return self.hp_max

    def getNamePerso(self):
        return self.name

    def getDicePerso(self):
        return self.dice

    def degats(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

    def soin(self, soin):
        self.hp += soin
        if self.hp > self.hp_max:
            self.hp = self.hp_max


class Hero(Personnage):
    def __init__(self, name, hp_max, dice, couleur='ffffff'):
        super().__init__(name, hp_max, dice)
        self.couleur = couleur


class Monstre(Personnage):
    pass
