from functions import *

pygame.init()
continuer = True

while continuer is True:
	screen = pygame.display.set_mode((800, 600))
	pygame.display.set_caption("Rapide comme l'alcool ?")

	background = (255, 255, 255)

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
