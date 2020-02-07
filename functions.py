# -*- coding: utf-8 -*-

import pygame
import random
import time
import socket
import sys
from pygame.locals import *


def show_result(screen, text):
	background = (255, 255, 255)
	set_background(screen, background)
	font = pygame.font.Font(None, 50)
	text = font.render("{}".format(text), True, (0, 0, 0), (255, 255, 255))
	textRect = text.get_rect()
	textRect.centerx = screen.get_rect().centerx
	textRect.centery = screen.get_rect().centery
	screen.blit(text, textRect)
	pygame.display.update()


def show_time(screen, time):
	font = pygame.font.Font(None, 30)
	text = font.render("{}".format(time), True, (0, 0, 0), (255, 255, 255))
	textRect = text.get_rect()
	textRect.x = screen.get_rect().x+5
	textRect.y = screen.get_rect().y+5
	screen.blit(text, textRect)
	pygame.display.update()


def set_background(screen, bg):
	screen.fill(bg)
	pygame.display.update()
