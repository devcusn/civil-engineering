
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

