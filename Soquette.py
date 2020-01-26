# -*- coding: utf-8 -*-
import socket
import time
from threading import Thread, Event
#################################################################
#                   CONFIGURATION DU SOCKET                     #
#################################################################
# IP et port du Tello
tello_address = ('192.168.10.1', 8889)

# Ajout du socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# On bind sur quel port on veut faire nos échanges
sock.bind(('', 9000))
# On ajoute un time out de 8 secondes
sock.settimeout(8)

#################################################################
#                   FONCTION POUR LES ACTIONS                   #
#################################################################
# Fonction pour envoyer un message à Tello
def send(message, sleep = 0):
  try:
    sock.sendto(message.encode(), tello_address)
    print("Sock envoi message: " + message)
  except Exception as e:
    print("Sock erreur envoi: " + str(e))

    # Un petit délai
  time.sleep(sleep)

# Fonction qui recoit un message de tello et l'affiche
def receive():
  try:
    response, ip_address = sock.recvfrom(128)
    print("receive-message recu : " + response.decode(encoding='utf-8') + " from Tello with IP: " + str(ip_address))
  except Exception as e:
    print("receive-erreur de reception : " + str(e))


# do_actions permet d'automatiser les actions pour le drone
def do_actions(action, sleep):
    
    send(action, sleep)

    # Réception du message recu de Tello
    receive()

    # Fermeture de la socket
    print("Le socket est clos")
 

 ##########################################################################
 # On utilise la fonction do_actions et on éxécute le programme dans main #
 # Si on veut ajouter une action alors il faudra créer un autre thread    #
 ##########################################################################
if __name__ == '__main__':
    print("------------------Debut du programme------------------")
    do_actions("command", 3)
    do_actions("sn?", 3)
    do_actions("battery?", 3)
   
 
    print("----------------Fin du programme-----------------")