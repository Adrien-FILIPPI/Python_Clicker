# -*- coding: utf-8 -*-

import pygame
import time
import random
from pygame.locals import *


def show_result(screen, text):
	font = pygame.font.Font(None, 50)
	text = font.render(" " * 100 + str(text) + " " * 100, True, (0, 0, 0))
	textRect = text.get_rect()

	textRect.centerx = screen.get_rect().centerx
	textRect.centery = screen.get_rect().centery

	screen.blit(text, textRect)
	pygame.display.update()


def show_time(screen, time):
	font = pygame.font.Font(None, 25)
	text = font.render(str(time) + " " * 100, True, (0, 0, 0))
	textRect = text.get_rect()

	textRect.x = screen.get_rect().x+5
	textRect.y = screen.get_rect().y+5

	screen.blit(text, textRect)
	pygame.display.update()
