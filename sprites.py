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
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.speed_x = 0
        self.jump_delay = 400
        self.last_jump = pg.time.get_ticks()
        self.jumping = False
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        KEYDOWN = pg.key.get_pressed()
        self.acc = vec(0, PLAYER_GRAV)
        if KEYDOWN[pg.K_LEFT] or KEYDOWN[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if KEYDOWN[pg.K_RIGHT] or KEYDOWN[pg.K_d]:
            self.acc.x = PLAYER_ACC
        if KEYDOWN[pg.K_SPACE] or KEYDOWN[pg.K_UP] or KEYDOWN[pg.K_w]:
            self.jump()

        # Friction
        self.acc.x += self.vel.x * PLAYER_FRIC
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0

        self.pos += self.vel


        if self.pos.x >= WIDTH:
            self.pos.x = 0.5

        if self.pos.x <= 0:
            self.pos.x = WIDTH

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
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass


