#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random

__appname__    = ""
__author__     = "Marco Sirabella"
__copyright__  = ""
__credits__    = ["Marco Sirabella"]  # Authors and bug reporters
__license__    = "GPL"
__version__    = "1.0"
__maintainer__ = "Marco Sirabella"
__email__      = "msirabel@gmail.com"
__status__     = "Prototype"  # "Prototype", "Development" or "Production"
__module__     = ""

pygame.init()
screen = pygame.display.set_mode((1000, 500))

debug = False
#debug = True

class Organism(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        """
        if temperment == "predator":
            color = (170, 57, 57)
        elif temperment == "prey":
            color = (64, 48, 117)
        elif temperment == "plant":
            color = (45, 136, 45)
        else:
            color = 255, 255, 255
        """
        #color = 0, 0, 0
        #if not self.size:
        #    self.size = (random.randint(4, 10)) # A good default starting size
        #self.image = pygame.Surface([self.size, self.size])
        self.image = pygame.Surface([self.size, self.size])
        self.image.fill((64, 48, 117))

        pygame.draw.rect(self.image, self.color, [0, 0, self.size, self.size])

        self.rect = self.image.get_rect()

        # Random Dispersal

        if self.startXcoord == 0 and self.startYcoord == 0:
            self.rect.x = random.uniform(0, 1000)
            self.rect.y = random.uniform(0, 500)
        else:
            #print(self.startXcoord)
            #print(self.startYcoord)
            self.rect.x = self.startXcoord - self.size / 2\
                + random.randint(-60, 60)
            self.rect.y = self.startYcoord - self.size / 2\
                + random.randint(-60, 60)

        # Statistic Distribution

        self.speed = random.uniform(0, 5)

class Plant(Organism):
    def __init__(self, coords=(0,0), growth=0):
        self.color = (45, 136, 45)
        self.size = random.randint(2, 7)
        # Only odd number of size
        self.size = (int(self.size/2)*2) + 1
        self.startXcoord = coords[0]
        self.startYcoord = coords[1]
        super().__init__()
        if not growth:
            self.growth = random.randint(0, 2)
        else:
            self.growth = growth
        # Above number is amount of pixels to grow on each side
        self.growth *= 2
        self.center_coords = (
            (self.rect.x * 2 + self.image.get_width()) / 2,
            (self.rect.y * 2 + self.image.get_height())/2)
        if debug:
            print("starting center coordinates: {1}\n\ngrowth: {0}\n\n".format(self.growth, self.center_coords))
    def tick(self, chance=0.99):
        #if True:
        if random.random() > chance:
            if debug:
                print("\
size: {0}\n\
xpos: {1}\n\
ypos: {2}\n\
xposE: {3}\n\
yposE: {4}\n\
center_point: {5}\n\
\n"\
                        .format(
                            self.size,
                            self.rect.x,
                            self.rect.y,
                            self.rect.x + self.image.get_width(),
                            self.rect.y + self.image.get_height(),
                            (
                                (self.rect.x + self.rect.x + self.image.get_width()) / 2,
                                (self.rect.y + self.rect.y + self.image.get_height())/2)
                            ))
            self.size += self.growth
            y = self.propagate()
        #y = self.propagate()
        #if True:
            if y:
                if random.random() > 0.75:
                #if 1 == 0:
                    # this looks confusing but its genetics
                    growth = self.growth/2 + round(random.uniform(-1, 1))
                    #print(growth)
                    #print('LALALALALALAL\nLALALALALALAL\nLALALALALALAL\n')
                else:
                    growth = self.growth / 2
                return y, growth
            self.scale(self.size)
    def scale(self, scalar):
        #size = self.size * 2
        #scalar *= 2
        if self.growth < 1:
        #if 1:
            # THIS DOESNT WORK
            self.image = pygame.transform.scale(self.image, (0, 0))
            self.kill()
            plant_list.remove(self)
        else:
            self.image = pygame.transform.scale(self.image, (scalar, scalar))
            #"""
            if not self.rect.y is 0 or 1:
                self.rect.y = self.rect.y - (self.growth / 2)
            else:
                self.rect.y = 0
            if not self.rect.x is 0 or 1:
                self.rect.x = self.rect.x - (self.growth / 2)
            else:
                self.rect.x = 0
        """
        if not self.rect.y is 0:
            self.rect.y = self.rect.y - (size) / (self.rect.y * size)
        else:
            self.rect.y = 0
        if not self.rect.x is 0:
            self.rect.x = self.rect.x - (size) / (self.rect.x * size)
        else:
            self.rect.x = 0
        """
    def propagate(self):
        #size = self.size * 2
        # #number below must be odd
        if self.size >= 20 and random.random() > 2/3:
            b4 = self.image.get_width()
            self.size = ((int(self.size/4)*2) - 1)
            self.scale(self.size)
            diff = b4 - self.image.get_width()
            if debug:
                print("before propagate: {0}\nafter propagate: {1}\n\n".format(b4, self.image.get_width()))
            self.rect.x = self.rect.x + diff/2 + self.growth/2
            self.rect.y = self.rect.y + diff/2 + self.growth/2
            return (
                (self.rect.x * 2 + self.image.get_width())/2,\
                (self.rect.y * 2 + self.image.get_height())/2
                )

            # self.rect.y = self.rect.y + (diff / (self.growth * 2/3)) - 1
    def testcol(self, sprite, ratio):
        test = pygame.sprite.collide_circle_ratio(ratio * self.size/7)
        if test(self, sprite):
            #print("{0} and {1} are near eachother".format(self, sprite))
            return True
    #def kill(self):
        # Remove sprite from all pygame groups
        #super().__init__()
        #plant_list.remove(self)
        #self = None
        #pass

        # Remove sprite from lists that add it to groups

class Animal(Organism):
    def __init__():
        pass


def plants():
    for x in plant_list:
        print(sprite_list.sprites)
        print(len(plant_list))
        y = x.tick(0)
        if y:
            if debug:
                print("parent grass center: {0}\n\nnumber of plant: {1}".format(y, len(plant_list)))
            grass = Plant(y[0], int(y[1]))
            sprite_list.add(grass)
            plant_list.append(grass)
        for y in plant_list:
            if x is not y:
                if x.testcol(y, 1):
                    if x.size * x.growth > y.size * y.growth:
                        y.kill()
                        plant_list.remove(y)
                    elif y.size * y.growth > x.size * x.growth:
                        if x in plant_list: plant_list.remove(x)
                        x.kill()
                    else:
                        print("hi")


sprite_list = pygame.sprite.Group()
plant_list = []
for x in range(0, 20):
    grass = Plant()
    sprite_list.add(grass)
    plant_list.append(grass)


carryOn = True
clock = pygame.time.Clock()
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if debug:
                print("ending center coordinates: {0}".format((
                    (plant_list[0].rect.x * 2 + plant_list[0].image.get_width()) / 2,
                    (plant_list[0].rect.y * 2 + plant_list[0].image.get_height())/2)))
            carryOn = False

    keys = pygame.key.get_pressed()

    #for x in range(0, 100):
    if 1 == 1:
        plants()
    #grass.rect.width = 50

    screen.fill((0, 0, 0))
    sprite_list.draw(screen)
    pygame.display.flip()

    clock.tick(60)
    #exit()
