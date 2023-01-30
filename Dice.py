from random import randint

class Dice:
    def __init__(self, faces):
        self.faces = faces

    def getFaceDice(self, face):
        return self.faces[face]

    def setFaceDice(self, face, effet):
        self.faces[face].effet = effet

    def tirerFace(self):
        return self.faces[randint(0,5)]


class Face:
    def __init__(self, effet, icon=None):
        self.effet = effet
        self.icon = icon

    def getEffetFace(self):
        return self.effet

