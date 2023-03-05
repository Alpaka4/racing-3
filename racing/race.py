import pygame
import sys
from  config_3 import *
from  grass import Grass
from  road import Road
from car import Car
from let import Let
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT))
grass=Grass("grass.jpg",screen,0,0)
grass_2=Grass("grass.jpg",screen,0,-1000)
road=Road("road_3.png",screen,150,0)
road_2=Road("road_3.png",screen,150,-1000)
car=Car("car.png",screen,(SCREEN_WIDTH)//2,(SCREEN_HEIGHT)//2)
let=Let("car_2.png",screen,0,0)
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

            
        
        grass.update()
        grass_2.update()
        road.update()
        road_2.update()
        car.update()
        let.update()
        screen.fill(BLACK)
        grass.draw()
        grass_2.draw()
        

        road.draw()
        road_2.draw()
        car.draw()
        let.draw()
        pygame.display.update()
        clock.tick(FPS)
