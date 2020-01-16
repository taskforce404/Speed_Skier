import pygame
from pygame.locals import *

def creat_font(language="chinese",size=10):
    if language == "chinese":
        path = "assets/fonts/black.TTF"
    else:
        path = None
    return pygame.font.Font(path,size)