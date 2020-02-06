import socket
import sys

HOST = '127.0.0.1'
PORT = 50000
counter = 0  # compteur de connexions actives

# création du socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# liaison du socket à une adresse précise :
try:
	mySocket.bind((HOST, PORT))
except socket.error:
	print("La liaison du socket à l'adresse choisie a échoué.")
	sys.exit()

while True:
	# Attente de la requête de connexion d'un client :
	print("Serveur prêt, en attente de requêtes ...")
	mySocket.listen(2)

	# Etablissement de la connexion :
	connexion, adresse = mySocket.accept()
	counter += 1
	print("Client connecté, adresse IP %s, port %s" % (adresse[0], adresse[1]))

	# Dialogue avec le client :
	msgServeur = "Vous êtes connecté au serveur Marcel. Envoyez vos messages."
	connexion.send(msgServeur.encode("Utf8"))
	msgClient = connexion.recv(1024).decode("Utf8")
	while True:
		print("C>", msgClient)
		if msgClient.upper() == "FIN" or msgClient == "":
			break
		msgServeur = input("S> ")
		connexion.send(msgServeur.encode("Utf8"))
		msgClient = connexion.recv(1024).decode("Utf8")
		print(ord(msgClient))

	# Fermeture de la connexion :
	connexion.send("fin".encode("Utf8"))
	print("Connexion interrompue.")
	connexion.close()

	ch = input("<R>ecommencer <T>erminer ? ")
	if ch.upper() == 'T':
		break
