from fly_tello import FlyTello
my_tellos = list()


# SIMPLE EXAMPLE - MOST BASIC FLIGHT TO SHOW STATUS MESSAGES
#
# SETUP: Any number of Tellos
#


#
# MAIN FLIGHT CONTROL LOGIC
#

# Define the Tello's we're using, in the order we want them numbered
my_tellos.append('0TQDG2KEDB4FH3')  # numéro 1 == DC5CE0
my_tellos.append('0TQDG2KEDBWK3X')  # numéro 2 == DC5F6C
# my_tellos.append('0TQDFCHEDB3F86')  # numéro 3 == D3FCE4
# my_tellos.append('0TQDG2KEDB04T1')  # numéro 4 == DC5CF3
# my_tellos.append('0TQDFCHEDBY3H0')  # numéro 5 == D3F926
# my_tellos.append('0TQDG2KEDBPE19')  # numéro 6 == DC5F05

print("longueur : ",len(my_tellos))

# parcours de la liste des tellos
with FlyTello(my_tellos, get_status=True) as fly:
    i = 0
    while i < len(my_tellos):
        fly.get_sn(i)
        fly.get_battery(i)
        i +=1
