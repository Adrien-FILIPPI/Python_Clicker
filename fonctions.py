import pygame
import time
import random
from pygame.locals import *


def show_result(screen, text):
	background = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
	set_background(screen, background)
	font = pygame.font.Font(None, 50)
	text = font.render(" " * 100 + str(text) + " " * 100, True, (0, 0, 0), background)
	textRect = text.get_rect()

	textRect.centerx = screen.get_rect().centerx
	textRect.centery = screen.get_rect().centery

	screen.blit(text, textRect)
	pygame.display.update()


def show_time(screen, time):
	font = pygame.font.Font(None, 25)
	text = font.render("Secondes restantes : " + str(time) + " " * 100, True, (0, 0, 0), background)
	textRect = text.get_rect()

	textRect.x = screen.get_rect().x+5
	textRect.y = screen.get_rect().y+5

	screen.blit(text, textRect)
	pygame.display.update()


def set_background(screen, bg):
	screen.fill(bg)
	pygame.display.update()
