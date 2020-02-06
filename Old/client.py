import socket
import sys

HOST = '127.0.0.1'
PORT = 50000

# création du socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# envoi d'une requête de connexion au serveur :
try:
	mySocket.connect((HOST, PORT))
except socket.error:
	print("La connexion a échoué.")
	sys.exit()
print("Connexion établie avec le serveur.")

# Dialogue avec le serveur :
msgServeur = mySocket.recv(1024).decode("Utf8")

while True:
	if msgServeur.upper() == "FIN" or msgServeur == "":
		break
	print("S>", msgServeur)
	msgClient = input("C> ")
	mySocket.send(msgClient.encode("Utf8"))
	msgServeur = mySocket.recv(1024).decode("Utf8")
	print(ord(msgServeur))

# Fermeture de la connexion :
print("Connexion interrompue.")
mySocket.close()
