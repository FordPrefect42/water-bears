#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

__appname__    = "Water Bears"
__author__     = "Marco Sirabella"
__copyright__  = ""
__credits__    = "Marco Sirabella, Christopher Adams"
__license__    = ""
__version__    = "0.0.1"
__maintainers__= "Marco Sirabella, Christopher Adams"
__email__      = "msirabel@gmail.com"
__status__     = "Prototype"
__module__     = ""

class variables(object):
    res = None
    size = None
    speed = [2, 2]
    black = 0, 0, 0
    orange = 255, 255, 0
    fullscreen = False
    screen = None
    def __init__(self):
        pygame.init()
        self.res = pygame.display.Info()
        self.screen_width = self.res.current_w
        self.screen_height = self.res.current_h
        self.size = width, height = (self.screen_width, self.screen_height)
        if self.fullscreen:
            self.screen = pygame.display.set_mode((self.size), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((self.size))
