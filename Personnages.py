class Personnage:
    def __init__(self, name, hp_max, dmg, soin):
        self.name = name
        self.hp_max = hp_max
        self.hp = hp_max
        self.dmg = dmg
        self.soin = soin

    def infligerDegats(self, target):
        target.subirDegats(self.dmg)

    def subirDegats(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

class Hero(Personnage):
    def soigner(self, target):
        target.hp += self.soin
        if target.hp > target.hp_max:
            target.hp = target.hp_max


class Monstre(Personnage):
    pass