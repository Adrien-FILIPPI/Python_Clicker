import socket
import select
import sys

HOST = "127.0.0.1"
PORT = 12800

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	mySocket.connect((HOST, PORT))
except socket.error:
	print("La liaison du socket à l'adresse choisie a échoué.")
	sys.exit()

print("Connexion établie avec le serveur sur le port {}".format(PORT))

msg_to_send = ""
while msg_to_send.upper() != "FIN":
	msg_to_send = input("> ")
	# Peut planter si vous tapez des caractères spéciaux
	msg_to_send = msg_to_send.encode("Utf8")
	# On envoie le message
	try:
		mySocket.send(msg_to_send)
		received_msg = mySocket.recv(1024)
		print(received_msg.decode("Utf8")) # Là encore, peut planter s'il y a des accents
	except:
		print("La connexion au serveur n'est plus active")


print("Fermeture de la connexion")
mySocket.close()
