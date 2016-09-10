#!/usr/bin/env python3

import sys
import pygame

#resolution = os.system("xrandr | grep '*' | cut -d ' ' -f 4 | head -n 1")
pygame.init()
resolution = pygame.display.Info()
pygame.quit()
#res = resolution
#size = width, height = (res.current_w, res.current_h)
print(resolution)

sys.exit(0)
