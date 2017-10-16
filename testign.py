from OgameBot import OgameBot
from GalaxySearcher import GalaxySearcher
from Requirements import getRequirementsTech
from planetState import PlanetState
from fleet import Fleet



testing = OgameBot()
testing.launchBrowser()
testing.login('michael93509@gmail.com','oOunv72Pg744nd2d45zo','uriel')
testing.getInfoFleets()
mainPlanet = PlanetState()
mainPlanet.set('Galaxy',4)
mainPlanet.set('Star',189)
mainPlanet.set('Planet','12')

print(testing.airborneFleets)



"""login: michael93452@gmail.com password: oOunv72Pg744nd2d45zo universe: Wezn"""
