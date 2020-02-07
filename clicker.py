from functions import *

pygame.init()
continuer = True

# Network
HOST = "51.77.151.88"
PORT = 80
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	mySocket.connect((HOST, PORT))
except socket.error:
	print("La liaison du socket à l'adresse choisie a échouée.")
	sys.exit()

print("Connexion établie avec le serveur sur le port {}".format(PORT))

data = []

received_msg = mySocket.recv(1024)
received_msg = received_msg.decode("Utf8")
data.append(received_msg)
nb_joueurs = data[0]
print("Nb joueurs : {}".format(nb_joueurs))

while continuer is True:
	screen = pygame.display.set_mode((800, 600))
	pygame.display.set_caption("Rapide comme l'alcool ?")
	background = (255, 255, 255)
	set_background(screen, background)
	font = pygame.font.Font(None, 50)

	result = 0

	text = font.render("En attente d'un joueur...", True, (0, 0, 0), (255, 255, 255))
	textRect = text.get_rect()
	textRect.centerx = screen.get_rect().centerx
	textRect.centery = screen.get_rect().centery
	screen.blit(text, textRect)
	pygame.display.update()

	timeleft = 5
	# show_time(screen, timeleft)

	continuer_jeu = True
	rejouer = True

	while continuer_jeu is True:
		if result > 0 and timeleft > 0:
			timeleft = 5-(int(time.time())-timestart)
			show_time(screen, timeleft)
		elif result > 0 >= timeleft:
			show_result(screen, "Ton score est de {} clics ! Tu es incroyable !".format(result))
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
		show_time(screen, "Appuyez sur Entrée pour revenir au salon")
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			continuer = False
			continuer_jeu = False
			rejouer = False
		if event.type == KEYDOWN:
			if event.key == K_RETURN:
				rejouer = False
				continuer_jeu = True
