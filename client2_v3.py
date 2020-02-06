import socket
import sys

HOST = "127.0.0.1"
PORT = 12800

is_client_on = True

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
score = "120"

try:
	mySocket.connect((HOST, PORT))
except socket.error:
	print("La liaison du socket à l'adresse choisie a échouée.")
	sys.exit()

print("Connexion établie avec le serveur sur le port {}".format(PORT))

received_msg = ""

while "boit" not in received_msg:
	msg_to_send = score
	msg_to_send = msg_to_send.encode("Utf8")
	# On envoie le message
	try:
		mySocket.send(msg_to_send)
		received_msg = mySocket.recv(1024)
		received_msg = received_msg.decode("Utf8")
		print(received_msg) # Là encore, peut planter s'il y a des accents
	except:
		print("La connexion au serveur n'est plus active")

print("Fermeture de la connexion")
mySocket.close()
