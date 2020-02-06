import socket
import select
import sys

HOST = "127.0.0.1"
PORT = 12800

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	mySocket.bind((HOST, PORT))
except socket.error:
	print("La liaison du socket à l'adresse choisie a échouée.")
	sys.exit()

mySocket.listen(5)
print("Le serveur écoute à présent sur le port {}".format(PORT))

is_server_on = True
connected_clients = []
client_score = []

while is_server_on:
	# On va vérifier que de nouveaux clients ne demandent pas à se connecter
	# Pour cela, on écoute la connexion_principale en lecture
	# On attend maximum 50ms
	requested_connections, wlist, xlist = select.select([mySocket], [], [], 0.05)

	for connection in requested_connections:
		connection_with_client, connection_infos = connection.accept()
		# On ajoute le socket connecté à la liste des clients
		connected_clients.append(connection_with_client)
		print("Client connecté, adresse IP %s, port %s" % (connection_infos[0], connection_infos[1]))

	# Maintenant, on écoute la liste des clients connectés
	# Les clients renvoyés par select sont ceux devant être lus (recv)
	# On attend là encore 50ms maximum
	# On enferme l'appel à select.select dans un bloc try
	# En effet, si la liste de clients connectés est vide, une exception
	# Peut être levée
	clients_to_read = []
	try:
		clients_to_read, wlist, xlist = select.select(connected_clients, [], [], 0.05)
	except select.error:
		pass
	else:
		# On parcourt la liste des clients à lire
		for client in clients_to_read:
			# Client est de type socket
			received_msg = client.recv(1024)
			# Peut planter si le message contient des caractères spéciaux
			received_msg = received_msg.decode("Utf8")
			print("Client : {}".format(received_msg))
			client_score.append(received_msg)
			if len(client_score) >= 2:
				score_j1 = client_score[0]
				score_j2 = client_score[1]
				if int(score_j1) > int(score_j2):
					nb_gorgees = int(score_j1) - int(score_j2)
					msg_to_send = "Le joueur qui n'a cliqué que " + str(score_j2) + " fois boit " + str(nb_gorgees) + " gorgées"
				elif score_j2 > score_j1:
					nb_gorgees = score_j2 - score_j1
					msg_to_send = "Mr " + str(score_j1) + " clics est le perdant. Il boit " + str(
						nb_gorgees) + " gorgées"
				else:
					msg_to_send = "Egalité - Personne ne boit :O ! "
				msg_to_send = msg_to_send.encode("Utf8")
				for i in range(len(connected_clients)):
					connected_clients[i].send(msg_to_send)


print("Fermeture des connexions")
for client in connected_clients:
	client.close()

mySocket.close()
