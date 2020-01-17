from fly_tello import FlyTello
my_tellos = list()

'''
// scenario specifique amphi MPG
// position initiale : 1 2 espacés de 50 cm
// 3 à 4 m d'espace
// TO DO : à terminer 
'''

#
# MAIN FLIGHT CONTROL LOGIC
#

# Define the Tello's we're using, in the order we want them numbered
my_tellos.append('0TQDG2KEDB4FH3')  # numéro 1 == DC5CE0
my_tellos.append('0TQDG2KEDBWK3X')  # numéro 2 == DC5F6C
#my_tellos.append('0TQDFCHEDB3F86')  # numéro 3 == D3FCE4
#my_tellos.append('0TQDG2KEDB04T1')  # numéro 4 == DC5CF3
#my_tellos.append('0TQDFCHEDBY3H0')  # numéro 5 == D3F926
#my_tellos.append('0TQDG2KEDBPE19')  # numéro 6 == DC5F05


# Control the flight
with FlyTello(my_tellos, get_status=True) as fly:
    # TO DO : battery_check 20
    fly.get_battery()
    fly.print_status(sync=True)
    fly.takeoff()
    fly.print_status(sync=True)
    # TO DO : ccw 90
    fly.up(80,1)
    fly.rotate_ccw(360,2)
    fly.forward(100,1)
    fly.down(80,1)
    fly.wait_sync()
    fly.up(80,2)
    fly.rotate_ccw(360,1)
    fly.forward(100,2)
    fly.down(80,2)
    fly.wait_sync()
    #fly.flip(f)
    fly.back(200)
    fly.print_status(sync=True)
    # TO DO : up 120
    #fly.print_status(sync=True)
    # TO DO : 1>forward 100
    #fly.print_status(sync=True)
    # TO DO : sync 2
    #fly.print_status(sync=True)
    # TO DO : 2>back 100
    #fly.print_status(sync=True)
    # TO DO : cw 90
    #fly.print_status(sync=True)
    fly.land()
    fly.print_status(sync=True)
