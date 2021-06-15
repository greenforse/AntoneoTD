
class Enemy():
    def __init__(self,road):
        self.speed = 10
        self.x = road.road[0][0]
        self.y = road.road[0][1]
        self.radius= 20
        self.napravlenia=[]
        self.HP=100
        self.step=1
    def go(self,road):
        rstep=False
        if self.x >= (road[self.step][0]-(self.speed+5)) and self.x <= (road[self.step][0]+(self.speed)) and self.y >= (road[self.step][1]-(self.speed)) and self.y <= (road[self.step][1]+(self.speed)) :
            while self.x%self.speed != 0 :
                self.x+=1
            while self.y%self.speed != 0:
                self.y+=1
            self.x = road[self.step][0]
            self.y = road[self.step][1]
            self.step+=1
            print("достигнут шаг",self.step)

        if self.x  <  road[self.step][0]:
            self.x +=self.speed
            print("+x")
            rstep=True
        elif self.x  >  road[self.step][0]  :
            if rstep:
                self.x -= (self.speed//2)
                print("Половина-х")
            else: 
                self.x -= self.speed
                print("-x")
            rstep=True
        if self.y < road[self.step][1] :
            if rstep:
                self.y += (self.speed//2)
            else:
                self.y += self.speed
            rstep=True
        elif self.y > road[self.step][1] :
            if rstep:
                self.y -= (self.speed//2)
            else: 
                self.y -= self.speed
            
        