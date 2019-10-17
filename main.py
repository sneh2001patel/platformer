# Bunny Hop Game with Kenny Sprites
import pygame as pg
import random
import time
from settings import *
from sprites import *

# main game class
class Game:
    def __init__(self):
        pg.init()
        self.display = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.spwandelay = 50;

    def run(self):
        # loop game
        self.clock.tick(FPS)
        print(self.clock.tick(FPS))
        while self.running:
            g.events()
            g.update()
            g.draw()

    def new(self):
        # new game
        # Platformer(x,y,w,h)
        self.all_sprites = pg.sprite.Group()
        self.platformer = pg.sprite.Group()
        self.plat0 = Platformer(self,WIDTH/2+45,HEIGHT/2+100,100,20)
        self.plat1 = Platformer(self,WIDTH/2-50,HEIGHT/2, 100,20)
        self.plat2 = Platformer(self,0,HEIGHT-20,WIDTH*4,20)
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.plat0)
        self.all_sprites.add(self.plat1)
        self.all_sprites.add(self.plat2)
        self.platformer.add(self.plat0)
        self.platformer.add(self.plat1)
        self.platformer.add(self.plat2)

        self.run()

    def events(self):
        # key bindings
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.running:
                    self.running = False


    def update(self):
        self.all_sprites.update()


        colide = pg.sprite.spritecollide(self.player, self.platformer, False)
        if self.player.vel.y > 0:
            for i in colide:
                if colide:
                    self.player.pos.y = i.rect.top +1
                    self.player.vel.y = 0


        if self.player.count == self.spwandelay:
            self.player.count = 0
            print("Match")
            self.a  = Platformer(self,random.randrange(WIDTH,WIDTH+110), random.randrange(HEIGHT/2-50,HEIGHT/2+50),100,20)
            self.all_sprites.add(self.a)
            self.platformer.add(self.a)



    def draw(self):
        # show game

        self.display.fill(BLACK)
        self.all_sprites.draw(self.display)
        pg.display.update()



g = Game()

while g.running:
    g.new()


print("BYEEEEEEEEE!!!!")
pg.quit()
quit()

