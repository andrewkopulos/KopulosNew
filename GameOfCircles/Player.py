import SpriteManager
from Sprite import Sprite
from Bullet import Bullet
class Player(Sprite):
    
    # instance variables
    left = False
    right = False
    up = False
    down = False
    speed = 4
    diameter = 50
    c = color(255,0,0)
    
    # constructor
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    # instance methods
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    #def handleCollision(self):
        #pass
        
    def move(self):
        if self.left:
            self.x -= self.speed
        if self.right:
            self.x += self.speed
        if self.up:
            self.y -= self.speed
        if self.down:
            self.y += self.speed
        self.x = constrain(self.x, self.diameter / 2, width - self.diameter / 2)
        self.y = constrain(self.y, self.diameter / 2, height - self.diameter / 2)
    
    def animate(self):
        self.display()
        self.move()
        
    def fire(self):
        print("FIRE")
        
    def keyDown(self):
        if key == 'f' or key == 'F':
            sprite.append(Bullet(self.x, self.y, PVector(0, -10), self.team))
    
        if keyCode == LEFT:
            self.left = True
        if keyCode == RIGHT:
            self.right = True
        if keyCode == UP:
            self.up = True
        if keyCode == DOWN:
            self.down = True
            
    def keyUp(self):
        if keyCode == LEFT:
            self.left = False
        if keyCode == RIGHT:
            self.right = False
        if keyCode == UP:
            self.up = False
        if keyCode == DOWN:
            self.down = False
