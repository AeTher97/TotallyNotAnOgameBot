from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class OgameBot:
    def getInfoResources(self):
        pass

    def getInfoBuildings(self):
        pass

    def getInfoTechnology(self):
        pass

    def getInfoSizeOfPlanet(self):
        pass

    def getInfoPlanetNumber(self):
        pass

    def launchBrowser(self):
        self.browser = webdriver.Chrome()
        self.browser.get(('https://pl.ogame.gameforge.com/'))

    def login(self,login,password,universe):
        commercialCloseButton = self.browser.find_element(By.XPATH,"//a[@href='javascript:;']")
        LoginWindowOpen = self.browser.find_element_by_id('loginBtn')
        usernameField = self.browser.find_element_by_id('usernameLogin')
        passwordField = self.browser.find_element_by_id('passwordLogin')
        serverField = self.browser.find_element_by_id('serverLogin')
        loginButton = self.browser.find_element_by_id('loginSubmit')

        commercialCloseButton.click()
        LoginWindowOpen.click()
        usernameField.send_keys(login)
        passwordField.send_keys(password)
        serverField.send_keys(universe)
        loginButton.click()

    def botWait(self):
        time.sleep(1)

    def changeScope(self, page):
        if page == 'overview':
            self.browser.get("https://s147-pl.ogame.gameforge.com/game/index.php?page=overview")
        if page == 'resources':
            self.browser.get("https://s147-pl.ogame.gameforge.com/game/index.php?page=resources")
        if page == 'station':
            self.browser.get("https://s147-pl.ogame.gameforge.com/game/index.php?page=station")
        if page == 'trader':
            self.browser.get("https://s147-pl.ogame.gameforge.com/game/index.php?page=traderOverview")
        if page == 'research':
            self.browser.get("https://s147-pl.ogame.gameforge.com/game/index.php?page=research")
        if page == 'shipyard':
            self.browser.get("https://s147-pl.ogame.gameforge.com/game/index.php?page=shipyard")
        if page == 'defense':
            self.browser.get("https://s147-pl.ogame.gameforge.com/game/index.php?page=defense")
        if page == 'fleet':
            self.browser.get("https://s147-pl.ogame.gameforge.com/game/index.php?page=fleet1")
        if page == 'galaxy':
            self.browser.get("https://s147-pl.ogame.gameforge.com/game/index.php?page=galaxy")
        if page == 'highScore':
            self.browser.get("https://s147-pl.ogame.gameforge.com/game/index.php?page=highscore")

    def build(self, building):
        resources = {'MetalMine': '1', 'CrystalMine' : '2' ,'DeuterExtractor' : '3', 'SolarPowerPlant' : '4',
                     'FusionPowerPlant' : '12', 'SolarSatellite' : '212', 'MetalStorage' : '22', 'CrystalStorage' : '23', 'DeuterStorage' : '24'}
        station = {'RobotFactory' : '14', 'Shipyard' : '21', 'Laboratory' : '31','AllayDepot' : '34' , 'RocketSilo' : '44', 'NaniteFactory' : '15', 'Terraformer' : '33', 'SpaceDock' : '36'}

        if building in resources:
            self.changeScope('resources')
            selection = "//a[@ref='" + resources[building] + "']"
            btnToClick = self.browser.find_element(By.XPATH,selection)
            btnToClick.click()
            WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//*[@id='content']/div[2]/a")))
            build = self.browser.find_element(By.XPATH,"//*[@id='content']/div[2]/a")
            build.click()
        if building in station:
            self.changeScope('station')
            selection = "//a[@ref='" + station[building] + "']"
            btnToClick = self.browser.find_element(By.XPATH,selection)
            btnToClick.click()
            WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content'']/div[2]/a")))
            build = self.browser.find_element(By.XPATH, "//*[@id='content']/div[2]/a")
            build.click()

    # TODO



"""login: michael93509@gmail.com password: oOunv72Pg744nd2d45zo: universe: Uriel"""


