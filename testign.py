from OgameBot import OgameBot


testing = OgameBot()
testing.launchBrowser()
testing.login('michael93452@gmail.com','testing1234','Wezn')
testing.getInfoResources()
testing.getInfoTechnology()
testing.getInfoBuildings()
testing.getInfoSizeOfPlanet()
testing.getInfoPlanetNumber()

print(testing.mainPlanetState)

testing.logout()