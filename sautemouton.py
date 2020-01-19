from fly_tello import FlyTello
my_tellos = list()

'''
// scenario specifique amphi MPG
// position initiale : 1 2 espacés de 100 cm
// 3 à 4 m d'espace
// TO DO : à terminer 
'''

#
# MAIN FLIGHT CONTROL LOGIC


# Define the Tello's we're using, in the order we want them numbered
my_tellos.append('0TQDG2KEDB4FH3')  # numéro 1 == DC5CE0
my_tellos.append('0TQDG2KEDBWK3X')  # numéro 2 == DC5F6C
#my_tellos.append('0TQDFCHEDB3F86')  # numéro 3 == D3FCE4
#my_tellos.append('0TQDG2KEDB04T1')  # numéro 4 == DC5CF3
#my_tellos.append('0TQDFCHEDBY3H0')  # numéro 5 == D3F926
#my_tellos.append('0TQDG2KEDBPE19')  # numéro 6 == DC5F05


def saute(i,j):
        # Le i se lève de 100
    fly.up(100,i)
    # Le j tourne sur lui même
    fly.rotate_ccw(360,j)
    # Le i avance de 150
    fly.forward(150,i)
    # Le j descend de 150
    fly.down(150,i)
    # synchronise
    fly.wait_sync()
    # Premier tour


# Control the flight
with FlyTello(my_tellos, get_status=True) as fly:
    fly.print_status(sync=True)
    fly.takeoff(sync=True)
    i,j = 1,2
    saute(i,j)
    i,j = 2,1
    saute(i,j)
    # fly.flip(f)
    fly.back(200,sync=True)
    fly.land()
    fly.print_status(sync=True)


