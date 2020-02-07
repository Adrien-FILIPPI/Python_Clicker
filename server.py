import socket
import select
import sys

HOST = "127.0.0.1"
PORT = 80

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	mySocket.bind((HOST, PORT))
except socket.error:
	print("La liaison du socket à l'adresse choisie a échouée.")
	sys.exit()

mySocket.listen(2)
print("Le serveur écoute à présent sur le port {}".format(PORT))

is_server_on = True
connected_clients = []
client_data = []

while is_server_on:
	requested_connections, wlist, xlist = select.select([mySocket], [], [], 0.05)
	for connection in requested_connections:
		connection_with_client, connection_infos = connection.accept()
		connected_clients.append(connection_with_client)
		print("Client connecté ! Adresse IP : {} - Port : {}".format(connection_infos[0], connection_infos[1]))
	nb_clients = len(connected_clients)

	for client in connected_clients:
		msg_to_send = "{}".format(nb_clients)
		msg_to_send = msg_to_send.encode("UTF-8")
		try:
			client.sendall(msg_to_send)
		except ConnectionResetError:
			print("Le client a été déconnecté")
			is_server_on = False

print("Fermeture des connexions")
for client in connected_clients:
	client.close()

mySocket.close()
