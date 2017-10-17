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

mainPlanet = PlanetState()
mainPlanet.set('Galaxy',4)
mainPlanet.set('Star',189)
mainPlanet.set('Planet',12)
testing.getInfoFleets()
print(testing.getInfoFleets())

cos = GalaxySearcher(testing)
cos.Colonize(10,mainPlanet)
testing.getInfoFleets()
print(testing.airborneFleets)

"""login: mich password: oOunv72Pg744nd2d45zo universe: Wezn"""
