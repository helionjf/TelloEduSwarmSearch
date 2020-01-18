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
    fly.left(200,1)
    fly.left(200,2)
    fly.left(200,3)
    fly.right(200,4)
    fly.right(200,5)
    fly.right(200,6)
    #deplacement escalier
    fly.up(100,1)
    fly.up(150,2)
    fly.up(200,3)
    fly.up(100,4)
    fly.up(150,5)
    fly.up(200,6)
    #deplacement avant de 400
    fly.forward(400)
    #rotation 90 dans le sens horaire pour 1, 2, 3 et anti horaire pour 4, 5, 6
    fly.rotate_cw(90,1)
    fly.rotate_cw(90,2)
    fly.rotate_cw(90,3)
    fly.rotate_ccw(90,4)
    fly.rotate_ccw(90,5)
    fly.rotate_ccw(90,6)
    #deplacement avant de 200
    fly.forward(200)
    #rotation 90
    fly.rotate_cw(90,1)
    fly.rotate_cw(90,2)
    fly.rotate_ccw(90,3)
    fly.rotate_ccw(90,4)
    #deplacement latéral de 400
    fly.forward(400)
    #rotation 180
    fly.rotate_ccw(180)
    #flip avant
    fly.flip("forward")
    fly.print_status(sync=True)
    #atterrisage
    fly.land()
    fly.print_status(sync=True)
