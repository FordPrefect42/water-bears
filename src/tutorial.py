#!/usr/bin/env python3

import sys
#from pygame.locals import *
import sprites

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

pygame = sprites.pygame
v = sprites.v

pygame.init()
v.res = pygame.display.Info()
v.screen_width = v.res.current_w
v.screen_height = v.res.current_h
v.size = width, height = (v.screen_width, v.screen_height)
#v.fullscreen = False
if v.fullscreen:
    v.screen = pygame.display.set_mode((v.size), pygame.FULLSCREEN)
else:
    v.screen = pygame.display.set_mode((v.size))

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

def keystrokes():
    global carryOn
    keys=pygame.key.get_pressed()
    # This causes some weird things to happen
    #if event.type == pygame.KEYDOWN:
    if v.fullscreen:
        if keys[pygame.K_ESCAPE]:
            carryOn = False
    else:
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            #print('LEFT')
            ch.rect.x -= 10
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            ch.rect.x += 10
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            #print('LEFT')
            ch.rect.y -= 10
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            ch.rect.y += 10
        return 0
    if 1==0:
        return 2
        #    if event.type == pygame.KEYDOWN:
       # if keys[


carryOn = True
clock = pygame.time.Clock()
#x = 1
all_sprites_list = pygame.sprite.Group()
def mid(beg, end):
    s = beg + end
    return (s / 2)

v.pos = (mid(0, v.screen_width), mid(0, v.screen_height))
ch = sprites.Character(v.pos, color=v.yellow)
all_sprites_list.add(ch)

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        carryOn = False



    v.screen.fill((0, 0, 0))
    ch.tick()
    """ Replaced by sprite tick definition """
    #all_sprites_list.draw(screen)
    pygame.display.flip()


    #if x == 1:
        #print(toggle_fullscreen())
        # Doesnt work


    clock.tick(60)
    #exit()
