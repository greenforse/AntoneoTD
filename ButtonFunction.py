
from FireTower import FireTower
from IceTower import IceTower
from LazerTower import LazerTower
def buyFireTower(player,cel,screen):
    newTower = FireTower (cel,screen)
    buyTower = player.buyTower(newTower.price) #Проверяем наличие золота у игрока и снимаем его 
    if buyTower:
        print("-20",player.gold)
        player.allTowers.append(newTower)
    else: print("Нету денюшек")
    print("Кyопка в меню нажата")
    #NewTower=FireTower(10,100,cel,sc)

def buyIceTower(player,cel,screen):
    newTower = IceTower (cel,screen)
    buyTower = player.buyTower(newTower.price) #Проверяем наличие золота у игрока и снимаем его 
    if buyTower:
        print("-20",player.gold)
        player.allTowers.append(newTower)
    else: print("Нету денюшек")
    print("Кyопка в меню нажата")

def buyLazerTower(player,cel,screen):
    newTower = LazerTower (cel,screen)
    buyTower = player.buyTower(newTower.price) #Проверяем наличие золота у игрока и снимаем его 
    if buyTower:
        print("-20",player.gold)
        player.allTowers.append(newTower)
    else: print("Нету денюшек")
    print("Кyопка в меню нажата")

def lvlUp(player,cel,sc):
    for tower in player.allTowers:
        if cel[0] <= tower.x + tower.wirina //2 and cel[0] >= tower.x-tower.wirina//2:
            if cel[1] <= tower.y + tower.dlina//2 and cel[1] >= tower.y-tower.dlina//2:
                player.lvlUp(tower)
                print("левел up")

def play(player,cel,sc):
    player.readyPlay()

def quit(player,cel,sc):
    pass