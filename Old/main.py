# -*- coding: utf-8 -*-

# from fonctions import *
import pygame
import time
import random
from pygame.locals import *

pygame.init()
continuer = True


def show_result(screen, text):
	global background
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


while continuer is True:

	screen = pygame.display.set_mode((800, 600))
	pygame.display.set_caption("Rapide comme l'alcool ?")

	background = (255, 255, 255)
	set_background(screen, background)

	screen.fill(background)
	pygame.display.update()
	font = pygame.font.Font(None, 50)

	result = 0

	text = font.render("Appuyez pour commencer", True, (0, 0, 0), (255, 255, 255))
	textRect = text.get_rect()

	textRect.centerx = screen.get_rect().centerx
	textRect.centery = screen.get_rect().centery

	screen.blit(text, textRect)
	pygame.display.update()

	timeleft = 15
	show_time(screen, timeleft)

	continuer_jeu = True
	rejouer = True

	while continuer_jeu is True:
		if result > 0 and timeleft > 0:
			timeleft = 15-(int(time.time())-timestart)
			show_time(screen, timeleft)
		elif result > 0 >= timeleft:
			show_result(screen, "Ton score est de : "+str(result)+" clics ! Tu es incroyable !")
			continuer_jeu = False
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			continuer = False
			continuer_jeu = False
			rejouer = False
		elif pygame.mouse.get_pressed()[0] and event.type == pygame.MOUSEBUTTONDOWN:
			if result == 0:
				timestart = int(time.time())
			result += 1
			show_result(screen, result)

	while rejouer is True:
		show_time(screen, "0. Pour rejouer, appuyer sur Entrée")
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			continuer = False
			continuer_jeu = False
			rejouer = False
		if event.type == KEYDOWN:
			if event.key == K_RETURN:
				rejouer = False
				continuer_jeu = True
