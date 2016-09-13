#!/usr/bin/env python3

import sys
import pygame
#from pygame.locals import *
import sprites

pygame.init()
res = pygame.display.Info()
screen_width = res.current_w
screen_height = res.current_h
size = width, height = (screen_width, screen_height)
speed = [2, 2]
black = 0, 0, 0
orange = 255, 255, 0
fullscreen = False
fullscreen = True
if fullscreen:
    screen = pygame.display.set_mode((size), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((size))

def toggle_fullscreen():
    """ From http://pygame.org/wiki/toggle_fullscreen """
    """ DOESNT WORK"""
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
all_sprites_list = pygame.sprite.Group()
def mid(beg, end):
    s = beg + end
    return (s / 2)

pos = (mid(0, screen_width), mid(0, screen_height))
print(pos)
ch = sprites.Character(pos, color=orange)
all_sprites_list.add(ch)

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    keys=pygame.key.get_pressed()
    if keys[pygame.KEYDOWN]:
        print('key is pressed')
    if keys[pygame.K_ESCAPE]:
        carryOn = False
    if keys[pygame.K_LEFT]:
        #print('LEFT')
        ch.rect.x -= 10
    if keys[pygame.K_RIGHT]:
        ch.rect.x += 10
    if keys[pygame.K_UP]:
        #print('LEFT')
        ch.rect.y -= 10
    if keys[pygame.K_DOWN]:
        ch.rect.y += 10
    if ch.rect.x < 0:
        ch.rect.x = screen_width - 1
    if ch.rect.x > screen_width:
        ch.rect.x = 1
    if ch.rect.y < 0:
        ch.rect.y = screen_height - 1
    if ch.rect.y > screen_height:
        ch.rect.y = 1


    screen.fill((0, 0, 0))
    all_sprites_list.draw(screen)
    pygame.display.flip()


    #if x == 1:
        #print(toggle_fullscreen())
        # Doesnt work


    clock.tick(60)
    #exit()
