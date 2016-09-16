#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import variables as v

__appname__    = "Water Bears"
__author__     = "Marco Sirabella"
__copyright__  = ""
__credits__    = "Marco Sirabella, Christopher Adams, Foo Bar"
__license__    = ""
__version__    = "0.0.1"
__maintainers__= "Marco Sirabella, Christopher Adams"
__email__      = "msirabel@gmail.com"
__status__     = "Prototype"
__module__     = ""

"""
This is where all sprites to be imported go
might be made into a package or module later on to save time
and organize
"""

pygame = v.pygame

Blue = (0, 0, 255)
WHITE = (255, 255, 255)
class Character(pygame.sprite.Sprite):
    def __init__(self, pos, img=None, color=Blue):
        super().__init__()
        if img:
            self.image = pygame.image.load(img).convert()
            self.image.set_colorkey(WHITE)
        else:
            self.image = pygame.Surface([20, 20])
            self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.sprites_list = pygame.sprite.Group()
        self.sprites_list.add(self)
    def tick(self):
        self.sprites_list.draw(v.screen)
        keys=pygame.key.get_pressed()

        """Key Input for movement"""
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            #print('LEFT')
            self.rect.x -= 10
            self.image.fill(v.blue)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += 10
            self.image.fill(v.orange)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            #print('LEFT')
            self.rect.y -= 10
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += 10

        """Screen looping"""
        if self.rect.x < 0:
            self.rect.x = v.screen_width# - 1
        if self.rect.x > v.screen_width:
            self.rect.x = 0# + 1
        if self.rect.y < 0:
            self.rect.y = v.screen_height# - 1
        if self.rect.y > v.screen_height:
            self.rect.y = 0# + 1
