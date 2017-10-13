from OgameBot import OgameBot


testing = OgameBot()

testing.launchBrowser()
testing.login('michael93509@gmail.com','oOunv72Pg744nd2d45zo','Uriel')
testing.getInfoResources()
testing.getInfoPlanetNumber()
testing.getInfoSizeOfPlanet()
testing.getInfoPlanetTemperature()

testing.getInfoPlanetPosition()



testing.build("RocketLauncher",1)
testing.botWait()
testing.botWait()
testing.build('SolarSatellite',1)

print(testing.mainPlanetState)

"""login: michael93452@gmail.com password: oOunv72Pg744nd2d45zo universe: Wezn"""
