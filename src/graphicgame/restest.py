#!/usr/bin/env python3

import sys
import pygame
import os

resolution = os.system("xrandr | grep '*' | cut -d ' ' -f 4 | head -n 1")
print(resolution)

