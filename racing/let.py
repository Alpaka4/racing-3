from config_3 import *
import pygame
import random
class Let(pygame.sprite.Sprite):
    def __init__(self,filename, screen,x,y):
        self.screen=screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image.set_colorkey(WHITE)
        self.image=pygame.transform.scale(self.image,(80,100))
        self.rect = self.image.get_rect()
        self.rect.x= x
        self.rect.y= y
        self.speedy=5
    def update(self):
        self.rect.y+=self.speedy
        let_x=[200,325,450,575]
        random.shuffle(let_x)
        for i in range(1):
            self.rect.x=let_x[0]
    def draw(self):
        self.screen.blit(self.image, self.rect)
