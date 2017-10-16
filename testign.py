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

fleet.set('LightFigher',1)
fleet.set('Speed',100)
fleet.set('Mission','Attack')


target= PlanetState()
target.set('Galaxy',4)
target.set('Star',193)
target.set('Planet',4)
print(target.get('Galaxy'))
print(target.get('Star'))
print(target.get('Planet'))
testing.sendFleet(fleet,target)



"""login: michael93452@gmail.com password: oOunv72Pg744nd2d45zo universe: Wezn"""
