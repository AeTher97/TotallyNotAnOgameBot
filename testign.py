from OgameBot import OgameBot
from GalaxySearcher import GalaxySearcher
from Requirements import getRequirementsTech
from planetState import PlanetState
from fleet import Fleet
from decisionMaking import find_steps
from decisionMaking import convert_steps_to_orders


testing = OgameBot()
testing.launchBrowser()
testing.login('michael93509@gmail.com','oOunv72Pg744nd2d45zo','uriel')

taki_jak_chce_osiagnac = PlanetState()
testing.getInfoAll()

taki_jak_chce_osiagnac.set('MetalMine',12)
taki_jak_chce_osiagnac.set('CrystalMine',10)
taki_jak_chce_osiagnac.set('DeuterExtractor',7)
taki_jak_chce_osiagnac.set('SolarPowerPlant',12)
taki_jak_chce_osiagnac.set('RobotFactory',4)
testing.changePlanet(2)

"""
for i in testing.mainPlanetState._attributes:
    print("planetState1.set(" + "'"+i+"'" + ", " + str(testing.mainPlanetState.get(i)) + ")")

zmienna = find_steps(testing.mainPlanetState,taki_jak_chce_osiagnac)

orders = convert_steps_to_orders(testing.mainPlanetState, zmienna)

"""


"""login: mich password: oOunv72Pg744nd2d45zo universe: Wezn"""
