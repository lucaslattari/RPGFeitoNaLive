from random import randint

class Enemy:
    def __init__(self):
        self.name = ''
        self.weapon = ''
        self.hp = 100

    def getRandomEnemy(self, mapName):
        if(mapName == 'China'):
           self.name = 'Panda'
           self.weapon = 'Bambu'
        elif(mapName == 'Brasil'):
            self.name = 'Biroliro'
            self.weapon = 'Revólver de Nióbio'
        elif(mapName == 'Polo Norte'):
           self.name = 'Urso Polar'
           self.weapon = 'Peixe'
        else:
            enemyId = randint(0, 2) % 3
            if(enemyId == 0):
                self.name = 'T-Rex'
                self.weapon = 'Urro Laser'
            elif(enemyId == 1):
                self.name = 'Velocipastor'
                self.weapon = 'Crucifixo'
            else:
                self.name = 'ET Bilu'
                self.weapon = 'Conhecimento'

        return self
