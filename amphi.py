from fly_tello import FlyTello
my_tellos = list()

'''
// scenario specifique amphi MPG
// position initiale : 1 2 3 4 5 6 (tous les drones à 12h)// table à midi
// TO DO : à terminer 
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
    for i in range(1,5):
        fly.takeoff(i)
        fly.pause(2)
    fly.print_status(sync=True)
    # tous montent de 1 m
    fly.up(100)
    #rotation 180 pour tous
    fly.rotate_cw(180)
    #deplacement latéral
    fly.left(200,1)
    fly.left(200,2)
    fly.right(200,3)
    fly.right(200,4)
    #deplacement escalier
    fly.up(20,1)
    fly.up(60,2)
    fly.up(20,3)
    fly.up(60,4)
    #fly.up(40,5)
    #fly.up(60,6)
    #deplacement avant de 400
    fly.forward(400)
    #rotation 90
    fly.rotate_cw(90,1)
    fly.rotate_cw(90,2)
    fly.rotate_ccw(90,3)
    fly.rotate_ccw(90,4)
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
