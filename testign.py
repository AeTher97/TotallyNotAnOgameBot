from OgameBot import OgameBot
from GalaxySearcher import GalaxySearcher
from Requirements import getRequirementsTech
from planetState import PlanetState
from fleet import Fleet



testing = OgameBot()
testing.launchBrowser()
testing.login('michael93509@gmail.com','oOunv72Pg744nd2d45zo','uriel')
mainPlanet = PlanetState()
mainPlanet.set('Galaxy',4)
mainPlanet.set('Star',189)
mainPlanet.set('Planet','12')
fleet = Fleet()
Fleet.set('LighFighter',1)
cos = GalaxySearcher(testing)
cos.scanGalaxy(5,mainPlanet)
cos.printList()
target= PlanetState()
target.set('Galaxy',4)
target.set('Star',193)
target.set('Planet',4)
OgameBot.sendFleet(Fleet,target,'Attack',100)



"""login: michael93452@gmail.com password: oOunv72Pg744nd2d45zo universe: Wezn"""
