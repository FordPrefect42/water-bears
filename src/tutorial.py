#!/usr/bin/env python3

import sys
import pygame
from pygame.locals import *

pygame.init()
res = pygame.display.Info()
size = width, height = (res.current_w, res.current_h)
speed = [2, 2]
black = 0, 0, 0
#screen = pygame.display.set_mode((size), pygame.FULLSCREEN)
screen = pygame.display.set_mode((size))

def toggle_fullscreen():
    """ From http://pygame.org/wiki/toggle_fullscreen """
    screen = pygame.display.get_surface()
    tmp = screen.convert()
    caption = pygame.display.get_caption()
    cursor = pygame.mouse.get_cursor()  # Duoas 16-04-2007

    w,h = screen.get_width(),screen.get_height()
    flags = screen.get_flags()
    bits = screen.get_bitsize()

    pygame.display.quit()
    pygame.display.init()

    screen = pygame.display.set_mode((w,h),flags^FULLSCREEN,bits)
    screen.blit(tmp,(0,0))
    pygame.display.set_caption(*caption)

    pygame.key.set_mods(0) #HACK: work-a-round for a SDL bug??

    pygame.mouse.set_cursor( *cursor )  # Duoas 16-04-2007

    return screen


carryOn = True
clock = pygame.time.Clock()
#x = 1
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    keys = pygame.key.get_pressed()

    screen.fill((0, 0, 0))
    #sprite_list.draw(screen)
    pygame.display.flip()


    #if x == 1:
        #print(toggle_fullscreen())
        # Doesnt work


    clock.tick(60)
    #exit()
