from functions import *

pygame.init()
continuer = True
nb_joueurs = "0"

screen = pygame.display.set_mode((800, 600), RESIZABLE)
pygame.display.set_caption("Rapide comme l'alcool ?")
background = (255, 255, 255)
set_background(screen, background)
font = pygame.font.Font(None, 50)

# Network
HOST = "51.77.151.88"
PORT = 8080
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	mySocket.connect((HOST, PORT))
except socket.error:
	print("La liaison du socket à l'adresse choisie a échouée.")
	sys.exit()

print("Connexion établie avec le serveur sur le port {}".format(PORT))

data = [""]

while "2" not in nb_joueurs:
	pygame.time.Clock().tick(30)
	received_msg = mySocket.recv(1024)
	received_msg = received_msg.decode("Utf8")
	data[0] = received_msg
	nb_joueurs = data[0]
	print("Nb joueurs : {}".format(nb_joueurs))
	text = font.render("En attente de joueurs...", True, (0, 0, 0), (255, 255, 255))
	textRect = text.get_rect()
	textRect.centerx = screen.get_rect().centerx
	textRect.centery = screen.get_rect().centery
	screen.blit(text, textRect)
	pygame.display.update()
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		sys.exit()
	else:
		pass

timeleft = 3
timestart_beforegame = int(time.time())
while timeleft > 0:
	timeleft = 3-(int(time.time())-timestart_beforegame)
	show_result(screen, "La partie commence dans {}".format(timeleft))
	time.sleep(0.1)

while continuer is True:
	result = 0

	continuer_jeu = True
	rejouer = True

	timeleft = 5

	while continuer_jeu is True:
		if result == 0:
			timestart = int(time.time())
			result += 1
			show_result(screen, result)
		elif result > 0 and timeleft > 0:
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
			result += 1
			show_result(screen, result)

	while rejouer is True:
		show_time(screen, "Appuyez sur Entrée pour revenir au salon")
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			continuer = False
			continuer_jeu = False
			rejouer = False
