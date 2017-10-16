from OgameBot import OgameBot
from GalaxySearcher import GalaxySearcher
from Requirements import getRequirementsTech
from planetState import PlanetState
from fleet import Fleet
from decisionMaking import find_steps
from decisionMaking import convert_steps_to_orders


testing = OgameBot()
testing.launchBrowser()
testing.login('michael93452@gmail.com','testing1234','wezn')
testing.getInfoFleets()
print(testing.airborneFleets)
testing.getInfoAll()
mainPlanet = PlanetState()
mainPlanet.set('Galaxy',4)
mainPlanet.set('Star',189)
mainPlanet.set('Planet',12)
print(testing.mainPlanetState)


new = testing.mainPlanetState.copy()
new.set('SpyProbe',1)
result = convert_steps_to_orders(testing.mainPlanetState,find_steps(testing.mainPlanetState,new))
for i in result:
    print(i)


"""login: mich password: oOunv72Pg744nd2d45zo universe: Wezn"""
