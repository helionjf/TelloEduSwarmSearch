from fly_tello import FlyTello
my_tellos = list()

'''
// scenario specifique amphi MPG
// position initiale : 1 2 espacés de 100 cm
// tous les deux à 15h
// 1 derrière le 2
// au millieu de l'estrade
//
// 
'''

#
# MAIN FLIGHT CONTROL LOGIC


# Define the Tello's we're using, in the order we want them numbered
#my_tellos.append('0TQDG2KEDB4FH3')  # numéro 1 == DC5CE0
#my_tellos.append('0TQDG2KEDBWK3X')  # numéro 2 == DC5F6C
#my_tellos.append('0TQDFCHEDB3F86')  # numéro 3 == D3FCE4
#my_tellos.append('0TQDG2KEDB04T1')  # numéro 4 == DC5CF3
my_tellos.append('0TQDFCHEDBY3H0')  # numéro 5 == D3F926
my_tellos.append('0TQDG2KEDBPE19')  # numéro 6 == DC5F05


def saute(i,j):
        # Le i se lève de 100
    fly.up(100,i)
    # Le j tourne sur lui même
    fly.rotate_ccw(360,j)
    # Le i avance de 150
    fly.forward(200,i)
    # Le i descend de 150
    fly.down(100,i)
    # synchronise
    fly.wait_sync()
    # Premier tour


# Control the flight
with FlyTello(my_tellos, get_status=True) as fly:
    fly.print_status(sync=True)
    fly.takeoff(sync=True)
    #fly.pad_detection_on()
    fly.up(50)
    k = 2
    while k > 0:
        saute(1,2)
        saute(2,1)
        fly.back(200,sync=True)
        k -=1
    #fly.straight_from_pad(x=0,y=10,z=20,speed=10,pad="m3",tello=1)
    #fly.straight_from_pad(x=0,y=10,z=20,speed=10,pad="m7",tello=2)
    fly.land()
    fly.pause(2)
    #fly.print_status(sync=True)
    fly.get_battery(sync=True)
    fly.get_sn()


