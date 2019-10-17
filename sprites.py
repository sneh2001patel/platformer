# Sprites for the game (Player, Platformer, Mobs, Collectable)
import pygame as pg
import random
import time
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (100, HEIGHT/2)
        self.speed_x = 0
        self.jump_delay = 400
        self.move_right = False
        self.move_left = False
        self.last_jump = pg.time.get_ticks()
        self.jumping = False
        self.pos = vec(100, HEIGHT/2)
        self.vel = vec(0.6, -0.8)
        self.acc = vec(0, 0)
        self.count = 0

    def update(self):
        self.move_right = False
        self.move_left = False
        KEYDOWN = pg.key.get_pressed()
        self.acc = vec(0, PLAYER_GRAV)
        if KEYDOWN[pg.K_LEFT] or KEYDOWN[pg.K_a]:
            self.acc.x = -PLAYER_ACC
            self.move_left = True
        if KEYDOWN[pg.K_RIGHT] or KEYDOWN[pg.K_d]:
            self.acc.x = PLAYER_ACC
            self.move_right = True
        if KEYDOWN[pg.K_SPACE] or KEYDOWN[pg.K_UP] or KEYDOWN[pg.K_w]:
            self.jump()

        print(self.count)
        if self.move_right:
            self.count += 1
        if self.move_left:
            self.count -= 1




        # Friction
        self.acc.x += self.vel.x * PLAYER_FRIC
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0

        self.pos += self.vel
        # print(self.vel)

        if self.pos.x >= WIDTH/2:
            self.pos.x = WIDTH/2

        if self.pos.x > 0 and self.pos.x < 100 and self.move_left:
            self.pos.x = 100
        self.rect.midbottom = self.pos

    def jump(self):
        now = pg.time.get_ticks()
        if now - self.last_jump > self.jump_delay:
            hit = pg.sprite.spritecollide(self, self.game.platformer, False)
            self.jumping = False
            self.last_jump = now
            if hit and self.jumping == False:
                self.vel.y = -PLAYER_JUMP
                self.jumping = True

class Platformer(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.rect.x = x
        self.rect.y = y
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)


    def update(self):
        self.acc = vec(0,0)
        self.speed_x = 0
        if self.game.player.pos.x >= WIDTH/2 and self.game.player.move_right:
            self.acc.x = -0.6
        if self.game.player.pos.x >=0 and self.game.player.pos.x <= WIDTH/4 and self.game.player.move_left:
            self.acc.x = 0.6

        # Friction
        self.acc.x += self.vel.x * PLAYER_FRIC
        self.vel += self.acc
        self.pos += self.vel

        self.rect.x = self.pos.x


