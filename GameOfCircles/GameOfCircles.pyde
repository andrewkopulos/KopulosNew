import platform
from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from Raindrop import Raindrop
from SpriteManager import sprites
from ScreenSaverBot import ScreenSaverBot
from JiggleBot import JiggleBot
import SpriteManager

def setup():
    print "Built with Processing Python version" + platform.python_version()
    global player, sprites
    size(500,500)
    playerTeam = 1
    enemyTeam = 2
    player= Player(width/2, height - 100, 1)
    
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(JiggleBot(175, 55, 2))
    SpriteManager.spawn(Enemy(55, 55, enemyTeam))
    SpriteManager.spawn(Raindrop(random(0, width), 10, enemyTeam))
    SpriteManager.spawn(Raindrop(random(0, width), 20, enemyTeam))
    SpriteManager.spawn(Raindrop(random(0, width), 30, enemyTeam))
    SpriteManager.spawn(Raindrop(random(0, width), 40, enemyTeam))
    SpriteManager.spawn(Raindrop(random(0, width), 40, enemyTeam))
    SpriteManager.spawn(ScreenSaverBot(30, 160, enemyTeam))
    SpriteManager.spawn(JiggleBot(height - 40, width/2, enemyTeam))
    
def draw():
    global player, sprites
    background(255)
    SpriteManager.animate()

def keyPressed():
    SpriteManager.player.keyDown()
    
def keyReleased():
    SpriteManager.player.keyUp()
