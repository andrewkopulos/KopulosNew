from Sprite import Sprite
from Bullet import Bullet
from Player import Player
import SpriteManager
class Enemy(Sprite):
    
    speed = 3
    diameter = 40
    c = color(0,0,255)
    mark = 0
    wait = 1000
    go = True
        
    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
            
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
            
    def aim(self, target):
        d = ((self.x - target.x)**2 + (self.y - target.y)**2)**.5
        xComponent = target.x - self.x
        yComponent = target.y - self.y
        xVector = xComponent/2 * .1
        yVector = yComponent/2 * .1
        return PVector(xVector, yVector)
    
    def fire(self, vector):
        if(millis() - self.mark > self.wait):
            self.go = not self.go
            self.mark = millis()
            
        if(self.go):
            self.go = False
            SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
