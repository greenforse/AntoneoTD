
from FireTower import FireTower

def buyFireTower(player,cel,screen):
    newTower = FireTower (10,100,cel,screen)
    buyTower = player.buyTower(newTower.price) #Проверяем наличие золота у игрока и снимаем его 
    if buyTower:
        print("-20",player.gold)
        player.allTowers.append(newTower)
    else: print("Нету денюшек")
    print("Кyопка в меню нажата")
    #NewTower=FireTower(10,100,cel,sc)