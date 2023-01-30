class Effet:
    def __init__(self, nom, couleur='ffffff'):
        self.nom = nom
        self.couleur = couleur

    def triggerEffet(self, target):
        return None

class EffetInfligerDegats(Effet):
    def __init__(self, nom, dmg):
        super().__init__(nom)
        self.dmg = dmg

    def triggerEffet(self, target):
        target.degats(self.dmg)

