from fly_tello import FlyTello
my_tellos = list()

'''
// table à midi
// 1=> au sol à 3 h
// 2=> sur la table à 3 h
'''
#
# SIMPLE EXAMPLE - MOST BASIC FLIGHT TO SHOW STATUS MESSAGES
#
# SETUP: Any number of Tellos
#


#
# MAIN FLIGHT CONTROL LOGIC
#

# Define the Tello's we're using, in the order we want them numbered
# my_tellos.append('0TQDG2KEDB4FH3')  # numéro 1 == DC5CE0
# my_tellos.append('0TQDG2KEDBWK3X')  # numéro 2 == DC5F6C
# my_tellos.append('0TQDFCHEDB3F86')  # numéro 3 == D3FCE4
# my_tellos.append('0TQDG2KEDB04T1')  # numéro 4 == DC5CF3
my_tellos.append('0TQDFCHEDBY3H0')  # numéro 5 == D3F926
my_tellos.append('0TQDG2KEDBPE19')  # numéro 6 == DC5F05


# Control the flight
with FlyTello(my_tellos, get_status=True) as fly:
    fly.get_battery(sync=True)
    fly.takeoff(sync=True)
    fly.up(100,1)
    fly.rotate_ccw(90,1)
    fly.rotate_cw(90,2)
    fly.forward(100,sync=True)
    fly.straight_from_pad(x=0,y=10,z=20,speed=10,pad="m5",tello=1)
    fly.straight_from_pad(x=0,y=10,z=20,speed=10,pad="m8",tello=2)
    fly.land()
    fly.print_status(sync=True)
