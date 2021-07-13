"""
Concrete Class
"""
class Concrete():
    def __init__(self,concrete_type,concrete_price='none'):
        print('creating a concrete object')
        self.concrete_type = concrete_type
        self.concrete_price = concrete_price
    def change_concrete_type(self,newValue):
        self.concrete_type = concrete_type
    def change_concrete_price(self,newValue):
        self.concrete_type = concrete_type
    def  CalculatePriceConcrete(self,m3):
        return m3 * self.concrete_price
    def __str__(self):
        return 'Concrete Type:{} \nConcrete_price: {}'.format(self.concrete_type,self.concrete_price)
    def __del__(self):
        print('{} is deleted'.format(self.concrete_type))

"""
Column Class
to use this class ,you have to create a
Concrete and Iron  by using Concrete class and
and Iron class
"""
class CreateColumn():
    def __init__(self,concrete,x,y,z):
        self.concrete = concrete.concrete_type
        self.concrete_price = concrete.concrete_price
        self.x = int(x)
        self.y = int(y)
        self.y = int(y)
        self.volume = x * y * z
        self.price = self.volume * self.concrete_price
    def  CalculatePriceColumns(self,piece):
        return piece * self.price
    def __str__(self):
        return 'Column Voice : {} \nColum Price {}'.format(self.volume,self.price)



"""
Beam Class
to use this class ,you have to create a
Concrete and Iron  by using Concrete class and
and Iron class
"""
class CreateBeam():
    def __init__(self,concrete,x,y,z):
        self.concrete = concrete.concrete_type
        self.concrete_price = concrete.concrete_price
        self.x = int(x)
        self.y = int(y)
        self.y = int(y)
        self.volume = x * y * z
        self.price = self.volume * self.concrete_price
    def  CalculatePriceBeam(self,piece):
        return piece * self.price
    def __str__(self):
        return 'Beam Voice : {} \nBeam Price {}'.format(self.volume,self.price)



"""
Brick Class
"""
class brick():
    def __init__(self,brickName,kg):
        self.brickName = brickName
        self.kg = kg
    def changeKg(self,newKg):
        self.kg = newKg
    def changeName(self,newName):
        self.brickName = newName
"""
Iron Class
"""        
class iron():
    def __init__(self,name,kg):
        self.kg = kg
        self.name = name
    def changeKg(self,newValue):
        self.kg = newValue
    def changeName(self,newName):
        self.newName
        
"""
Floor Class
to use this class, you have to create Column and Beam
by using Column and Beam Class
"""
"""
birdeye :
[
 [1,0,0,1,0,0,1],
 [0,2,2,0,2,2,0],
 [1,0,0,1,0,0,1],
 [0,2,2,0,2,2,0],
 [1,0,0,1,0,0,1]
]
"""
class floor():
    def __init__(self,column,columnNumber,beam,beamNumber,birdeye):
        self.columnNumber = columnNumber
        self.beamNumber = beamNumber
        self.column = column
        self.beam = beam
        self.totalVoiceColumn = self.column.volume * self.columnNumber
        self.totalVoiceBeam = self.beam.volume * self.beamNumber
        self.totalVoice = self.totalVoiceColumn + self.totalVoiceBeam
        self.birdeye = birdeye
    def showAll(self):

        for i in self.birdeye:
            b = []
            for a in i:
                if(a == 0):
                    b.append(' - ')
                elif(a ==1):
                    b.append(' + ')
                else:
                    b.append('   ')

            print(''.join(b))


        
"""
Building Class
to use this class, you hace to create
floor by using floor class
"""
class Building():
    def __init__(self,floor,floorNumber):
        self.totalFloorNumber = floorNumber
        self.totalVoice = floor.totalVoice
        self.totalMass = floor.mass

concrete = Concrete('c300',500)
column = CreateColumn(concrete,5,5,6)
matris = [
 [1,0,0,1,0,0,1],
 [0,2,2,0,2,2,0],
 [1,0,0,1,0,0,1],
 [0,2,2,0,2,2,0],
 [1,0,0,1,0,0,1]
]
beam = CreateBeam(concrete,5,5,15)
floor = floor(column,6,beam,6,matris)
floor.showAll()
