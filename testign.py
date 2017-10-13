from OgameBot import OgameBot


testing = OgameBot()
testing.launchBrowser()
testing.login('michael93452@gmail.com','testing1234','Wezn')
testing.getInfoResources()
testing.getInfoFleetSize()

print(testing.mainPlanetState)

testing.logout()