from player import Player
from map import Map
from enemy import Enemy

def showTitleScreen():
    titleFrame1 = '''
 ▄▀▀█▄▄   ▄▀▀█▀▄    ▄▀▀█▄       ▄▀▀▄ ▀▄  ▄▀▀▀▀▄   ▄▀▀▄▀▀▀▄  ▄▀▀▄ ▄▀▄  ▄▀▀█▄   ▄▀▀▀▀▄
█ ▄▀   █ █   █  █  ▐ ▄▀ ▀▄     █  █ █ █ █      █ █   █   █ █  █ ▀  █ ▐ ▄▀ ▀▄ █    █
▐ █    █ ▐   █  ▐    █▄▄▄█     ▐  █  ▀█ █      █ ▐  █▀▀█▀  ▐  █    █   █▄▄▄█ ▐    █
  █    █     █      ▄▀   █       █   █  ▀▄    ▄▀  ▄▀    █    █    █   ▄▀   █     █
 ▄▀▄▄▄▄▀  ▄▀▀▀▀▀▄  █   ▄▀      ▄▀   █     ▀▀▀▀   █     █   ▄▀   ▄▀   █   ▄▀    ▄▀▄▄▄▄▄▄▀
█     ▐  █       █ ▐   ▐       █    ▐            ▐     ▐   █    █    ▐   ▐     █
▐        ▐       ▐             ▐                           ▐    ▐              ▐
'''

    titleFrame2 = '''
██▄   ▄█ ██          ▄   ████▄ █▄▄▄▄ █▀▄▀█ ██   █
█  █  ██ █ █          █  █   █ █  ▄▀ █ █ █ █ █  █
█   █ ██ █▄▄█     ██   █ █   █ █▀▀▌  █ ▄ █ █▄▄█ █
█  █  ▐█ █  █     █ █  █ ▀████ █  █  █   █ █  █ ███▄
███▀   ▐    █     █  █ █         █      █     █     ▀
           █      █   ██        ▀      ▀     █
          ▀                                 ▀
    '''

    import time,os

    startTime = time.time()   #Tempo de inicio
    currentTime = time.time() #Tempo atual
    counter = 0

    while(currentTime < startTime + 5.0):
        if(counter % 2 == 0):
            print(titleFrame1)
        else:
            print(titleFrame2)
        counter += 1

        time.sleep(0.4)
        os.system("cls")
        currentTime = time.time()

def main():
    showTitleScreen()
    p = Player()
    m = Map()
    e = Enemy()
    chosenMap = m.getRandomMap()
    print('Você acordou em', chosenMap, 'sem saber como veio parar aqui...')
    randomEnemy = e.getRandomEnemy(chosenMap)
    print('Oh! Você se deparou com o ' + randomEnemy.name + '.\nEle vai te atacar com ' + randomEnemy.weapon + '!')


main()
