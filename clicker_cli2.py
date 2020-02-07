from functions import *

pygame.init()
continuer = True
nb_joueurs = "0"

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

data = []

while nb_joueurs != "2":
	received_msg = mySocket.recv(1024)
	received_msg = received_msg.decode("Utf8")
	data.append(received_msg)
	nb_joueurs = data[0]
	print("Nb joueurs : {}".format(nb_joueurs))

while continuer is True:
	result = 0
	continuer_jeu = True
	timeleft = 5

	while continuer_jeu is True:
		if result > 0 and timeleft > 0:
			timeleft = 5-(int(time.time())-timestart)
			print(timeleft)
		elif result > 0 >= timeleft:
			print("Ton score est de {} clics ! Tu es incroyable !".format(result))
			continuer_jeu = False
			continuer = False
		if result == 0:
			timestart = int(time.time())
		result += 1
		print("{}".format(result))
