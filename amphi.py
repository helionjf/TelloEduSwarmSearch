from fly_tello import FlyTello
my_tellos = list()

'''
// scenario specifique amphi MPG
// position initiale : 1 2 3 4 5 6 (tous les drones à 12h)// table à midi
// Attention à séparer les drones d'au moins 1,5 m
// Les drones sont tournés vers l'opérateur et font dos à la salle
'''

#
# MAIN FLIGHT CONTROL LOGIC
#

# Define the Tello's we're using, in the order we want them numbered
my_tellos.append('0TQDG2KEDB4FH3')  # numéro 1 == DC5CE0
my_tellos.append('0TQDG2KEDBWK3X')  # numéro 2 == DC5F6C
my_tellos.append('0TQDFCHEDB3F86')  # numéro 3 == D3FCE4
my_tellos.append('0TQDG2KEDB04T1')  # numéro 4 == DC5CF3
my_tellos.append('0TQDFCHEDBY3H0')  # numéro 5 == D3F926
my_tellos.append('0TQDG2KEDBPE19')  # numéro 6 == DC5F05


# Control the flight
with FlyTello(my_tellos, get_status=True) as fly:
    # TO DO : battery_check 20
    fly.get_battery()
    fly.print_status(sync=True)
    # tous décolent à 2 secondes d'écart
    for i in range(1,7):
        fly.takeoff(i)
        fly.pause(2)
    fly.print_status(sync=True)
    # tous montent de 1 m
    fly.up(100)
    # rotation 180 pour tous afin d'être face à la salle
    fly.rotate_cw(180)
    #deplacement latéral, 1, 2 ,3 vers la gauche et 4, 5, 6 vers la droite
    for i in range(1,4):
        fly.left(200,i)
    for i in range(4,7):
        fly.right(200,i)
    #deplacement escalier assez espacé pour éviter les collisions
    '''for i in (1,6):
        fly.up(80,i)
    for i in (2,5):
        fly.up(60,i)
    for i in (3,4):
        fly.up(40,i)'''
    #deplacement synchronisé avant de 400
    fly.forward(400,sync=True)
    #rotation 90 dans le sens horaire pour 1, 2, 3 et anti horaire pour 4, 5, 6
    for i in range(1,4):
        fly.rotate_cw(90,i)
    for i in range(4,7):
        fly.rotate_ccw(90,i)
    #deplacement synchronisé avant de 200 pour revenir vers le centre
    fly.forward(200,sync=True)
    #rotation 90 dans le sens horaire pour 1, 2, 3 et anti horaire pour 4, 5, 6
    for i in range(1,4):
        fly.rotate_cw(90,i)
    for i in range(4,7):
        fly.rotate_ccw(90,i)
    #vitesse maximum pour tous
    fly.set_speed(speed=100,sync=True)
    #deplacement avant synchronisé de 450 pour revenir vers l'opérateur. un peu plus de 400 pour être sûr de ne pas atterrir sur les spectateurs
    fly.forward(dist=450,sync=True)
    #rotation 180 pour faire face à la salle
    fly.rotate_ccw(180,sync=True)
    #flip avant
    fly.flip("forward",sync=True)
    # on descend de 150 cm
    fly.down(150)
    # on se retourne vers l'opérateur
    fly.rotate_cw(180)
    #on remet la vitesse à 10
    fly.set_speed(speed=10)    
    #atterrisage
    fly.land(sync=True)
    fly.print_status(sync=True)
