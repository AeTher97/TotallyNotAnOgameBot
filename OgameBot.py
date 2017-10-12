from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re


class OgameBot:

    _resources = {'MetalMine': '1', 'CrystalMine': '2', 'DeuterExtractor': '3', 'SolarPowerPlant': '4',
                 'FusionPowerPlant': '12', 'SolarSatellite': '212', 'MetalStorage': '22', 'CrystalStorage': '23',
                 'DeuterStorage': '24'}
    _station = {'RobotFactory': '14', 'Shipyard': '21', 'Laboratory': '31', 'AllayDepot': '34', 'RocketSilo': '44',
               'NaniteFactory': '15', 'Terraformer': '33', 'SpaceDock': '36'}

    _resourcesLevels = {'MetalMine': 0, 'CrystalMine': 0, 'DeuterExtractor': 0, 'SolarPowerPlant': 0,
                       'FusionPowerPlant': 0, 'SolarSatellite': 0, 'MetalStorage': 0, 'CrystalStorage': 0,
                       'DeuterStorage': 0}
    _stationLevels = {'RobotFactory': 0, 'Shipyard': 0, 'Laboratory': 0, 'AllayDepot': 0, 'RocketSilo': 0,
                     'NaniteFactory': 0, 'Terraformer': 0, 'SpaceDock': 0}
    _planetNumber=0
    _planetSize=0

    def getInfoResources(self):
        self.setScope('overview')
        metal = self.browser.find_element_by_id('resources_metal').text
        crystal = self.browser.find_element_by_id('resources_crystal').text
        deuter = self.browser.find_element_by_id('resources_deuterium').text
        energy = self.browser.find_element_by_id('resources_energy').text
        print(metal)
        print(crystal)
        print(deuter)
        print(energy)
        
    def getInfoBuildings(self):
        self.setScope('resources')
        for building in self._resources:
            if building!='SolarSatellite':
                selection = "//a[@ref='" + self._resources[building] + "']"
                btnToClick = self.browser.find_element(By.XPATH, selection)
                btnToClick.click()
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content']/div[2]/a")))

                level = int(re.search(r'\d+', self.browser.find_element_by_xpath("//*[@id='content']/span").text).group())
                self._resourcesLevels[building] = level

        self.setScope('station')
        for building in self._station:
            if building!='Laboratory':
                selection = "//a[@ref='" + self._station[building] + "']"
                btnToClick = self.browser.find_element(By.XPATH, selection)
                btnToClick.click()
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content']/div[2]/a/span")))
                level = int(re.search(r'\d+',self.browser.find_element_by_xpath("//*[@id='content']/span").text).group())
                self._stationLevels[building] = level
            if building == 'Laboratory':
                selection = "//a[@ref='" + self._station[building] + "']"
                btnToClick = self.browser.find_element(By.XPATH, selection)
                btnToClick.click()
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content']/div[2]/a")))
                level = int(re.search(r'\d+',self.browser.find_element_by_xpath("//*[@id='content']/span").text).group())
                self._stationLevels[building] = level

        for element in self._resourcesLevels:
            print(element)
            print(self._resourcesLevels[element])
        for element in self._stationLevels:
            print(element)
            print(self._stationLevels[element])

    def getInfoTechnology(self):
        pass

    def getInfoSizeOfPlanet(self):
        self.setScope('overview')
        self._planetSize = self.browser.find_element_by_xpath("//*[@id='diameterContentField']/span[2]").text
        print(self._planetSize)


    def getInfoPlanetNumber(self):
        self.setScope('overview')
        string = self.browser.find_element_by_xpath("//*[@id='countColonies']/p/span").text
        self._planetNumber=string[2]

    def launchBrowser(self):
        self.browser = webdriver.Chrome()
        self.browser.get(('https://pl.ogame.gameforge.com/'))

    def login(self, login, password, universe):
        commercialCloseButton = self.browser.find_element(By.XPATH, "//a[@href='javascript:;']")
        LoginWindowOpen = self.browser.find_element_by_id('loginBtn')
        usernameField = self.browser.find_element_by_id('usernameLogin')
        passwordField = self.browser.find_element_by_id('passwordLogin')
        serverField = self.browser.find_element_by_id('serverLogin')
        loginButton = self.browser.find_element_by_id('loginSubmit')

        commercialCloseButton.click()
        LoginWindowOpen.click()
        for i in login:
            usernameField.send_keys(i)
        for i in password:
            passwordField.send_keys(i)
        serverField.send_keys(universe)
        loginButton.click()

        self.current_scope = "overview"

    def botWait(self):
        time.sleep(1)

    def setScope(self, page):
        """
        :param page: string: on of these: overview, resources, station, traderOverwie, research, shipyard, defense, fleet, galaxy, highscore
        :return: Nothing
        """
        currentURL = self.browser.current_url
        uninumber = currentURL[9] + currentURL[10] + currentURL[11]

        if (self.current_scope == page):
            return
        if page == 'fleet':
            self.browser.get("https://s"+uninumber+"-pl.ogame.gameforge.com/game/index.php?page=fleet1")
        else:
            self.browser.get("https://s"+uninumber+"-pl.ogame.gameforge.com/game/index.php?page=" + page)
        self.current_scope = page

    def build(self, building):


        if building in self._resources:
            self.setScope('resources')
            selection = "//a[@ref='" + self._resources[building] + "']"
            btnToClick = self.browser.find_element(By.XPATH, selection)
            btnToClick.click()
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content']/div[2]/a")))
            build = self.browser.find_element(By.XPATH, "//*[@id='content']/div[2]/a")
            build.click()
        if building in self._station:
            self.setScope('station')
            selection = "//a[@ref='" + self._station[building] + "']"
            btnToClick = self.browser.find_element(By.XPATH, selection)
            btnToClick.click()
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content'']/div[2]/a")))
            build = self.browser.find_element(By.XPATH, "//*[@id='content']/div[2]/a")
            build.click()


            # TODO


"""login: michael93452@gmail.com password: testing1234 universe: Wezn"""


