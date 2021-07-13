class brick():
    def __init__(self,brickName,kg):
        self.brickName = brickName
        self.kg = kg
    def changeKg(self,newKg):
        self.kg = newKg
    def changeName(self,newName):
        self.brickName = newName
