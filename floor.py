"""
cordinate = [
[1,2,1,2,1],
[2,0,2,0,2],
[1,2,1,2,1]
]
before use this class,you must to create column and beam by using
column and beam class
"""
class floor():
    def __init__(self,column,columnNumber,beam,beamNumber,cordinate):
        self.columnNumber = columnNumber
        self.beamNumber = beamNumber
        self.column = column
        self.beam = beam
        self.totalVoiceColumn = self.column.volume * self.columnNumber
        self.totalVoiceBeam = self.beam.volume * self.beamNumber
        self.totalVoice = self.totalVoiceColumn + self.totalVoiceBeam
        self.cordinate = cordinate
    def showAll(self):
        print('everyting')
    
