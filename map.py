from random import randint

class Map:
    def __init__(self):
        self.map = ['China', 'Brasil', 'Polo Norte', 'Acre']
        
    def getRandomMap(self):
        mapId = randint(0, len(self.map) - 1)
        return self.map[mapId]
