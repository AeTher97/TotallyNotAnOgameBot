from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
from planetState import PlanetState


class OgameBot:
    def __init__(self):
        self._resources = {'MetalMine': '1',
                           'CrystalMine': '2',
                           'DeuterExtractor': '3',
                           'SolarPowerPlant': '4',
                           'FusionPowerPlant': '12',
                           'MetalStorage': '22',
                           'CrystalStorage': '23',
                           'DeuterStorage': '24'}
        self._station = {'RobotFactory': '14',
                         'Shipyard': '21',
                         'Laboratory': '31',
                         'AllayDepot': '34',
                         'RocketSilo': '44',
                         'NaniteFactory': '15',
                         'Terraformer': '33',
                         'SpaceDock': '36'}

        self._research = {'EnergyTechnology': '113',
                          'LaserTechnology': '120',
                          'IonTechnology': '121',
                          'HyperspaceTechnology': '114',
                          'PlasmaTechnology': '122',
                          'CombustionDrive': '115',
                          'ImpulseDrive': '117',
                          'HyperDrive': '118',
                          'SpyTechnology': '106',
                          'ComputerTechnology': '108',
                          'Astrophysics': '124',
                          'IntergalacticResearchNetwork': '123',
                          'GravitonDevelopment': '199',
                          'BattleTechnology': '109',
                          'ShieldingTechnology': '110',
                          'Armor': '111'}

        self._fleet = {'LightFigher': '204',
                       'HeavyFigher': '205',
                       'Cruiser': '206',
                       'Battleship': '207',
                       'LightTransport': '202',
                       'HeavyTransport': '203',
                       'ColonizationShip': '208',
                       'Dreadnought': '215',
                       'Bomber': '211',
                       'Destroyer': '213',
                       'DeathStar': '214',
                       'Recycler': '209',
                       'SpyProbe': '210',
                       'SolarSatellite': '212'}

        self._defense = {'RocketLauncher': '401',
                         'LightLaserCannon': '402',
                         'HeavyLaserCannon': '403',
                         'GaussCannon': '404',
                         'IonCannon': '405',
                         'PlasmaLauncher': '406',
                         'SmallPlanetaryShield': '407',
                         'LargePlanetaryShield': '408',
                         'AntiMissile': '502',
                         'InterplanetaryMissile': '503'}

        self.current_scope = ""
        self.browser = None
        self.mainPlanetState = PlanetState()
        self.planetNumber = 0

    def getInfoResources(self):
        self.setScope('overview')
        metal = self.browser.find_element_by_id('resources_metal').text
        crystal = self.browser.find_element_by_id('resources_crystal').text
        deuter = self.browser.find_element_by_id('resources_deuterium').text
        energy = self.browser.find_element_by_id('resources_energy').text

        self.mainPlanetState.set("metal", metal)
        self.mainPlanetState.set("crystal", crystal)
        self.mainPlanetState.set("deuter", deuter)
        self.mainPlanetState.set("energy", energy)

    def getInfoBuildings(self):
        self.setScope('resources')
        for building in self._resources:
            if building != 'SolarSatellite':
                selection = "//a[@ref='" + self._resources[building] + "']"
                btnToClick = self.browser.find_element(By.XPATH, selection)
                btnToClick.click()
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content']/div[2]/a")))

                level = int(re.search(r'\d+', self.browser.find_element_by_xpath(
                    "//*[@id='content']/span").text).group())
                self.mainPlanetState.set(building, level)

        self.setScope('station')
        for building in self._station:

            selection = "//a[@ref='" + self._station[building] + "']"
            btnToClick = self.browser.find_element(By.XPATH, selection)
            btnToClick.click()
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content']/div[2]/a/span")))
            level = int(re.search(r'\d+', self.browser.find_element_by_xpath("//*[@id='content']/span").text).group())
            self.mainPlanetState.set(building, level)


    def getInfoTechnology(self):
        self.setScope('research')

        for research in self._research:

            selection = "//a[@ref='" + self._research[research] + "']"
            btnToClick = self.browser.find_element(By.XPATH, selection)
            btnToClick.click()
            WebDriverWait(self.browser, 10).until(
                 EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content']/div[2]/a")))

            level = int(re.search(r'\d+', self.browser.find_element_by_xpath("//*[@id='content']/span").text).group())
            self.mainPlanetState.set(research, level)

    def getInfoFleetSize(self):
        self.setScope('shipyard')

        for ship in self._fleet:
            selection = "//a[@ref='" + self._fleet[ship] + "']"
            btnToClick = self.browser.find_element(By.XPATH, selection)
            btnToClick.click()
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_all_elements_located((By.ID, "number")))

            number = int(re.search(r'\d+', self.browser.find_element_by_xpath("//*[@id='content']/span").text).group())
            self.mainPlanetState.set(ship, number)

    def getInfoDefenses(self):
        self.setScope('defense')

        for defense in self._defense:
            selection = "//a[@ref='" + self._defense[defense] + "']"
            btnToClick = self.browser.find_element(By.XPATH, selection)
            btnToClick.click()
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_all_elements_located((By.ID, "number")))

            number = int(re.search(r'\d+', self.browser.find_element_by_xpath("//*[@id='content']/span").text).group())
            self.mainPlanetState.set(defense, number)

    def getInfoSizeOfPlanet(self):
        self.setScope('overview')
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[@id='diameterContentField']/span[2]")))
        planetSize = self.browser.find_element(By.XPATH, "//*[@id='diameterContentField']/span[2]").text
        self.mainPlanetState.set('PlanetSize', planetSize)

    def getInfoPlanetTemperature(self):
        self.setScope('overview')
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[@id='honorContentField']")))
        self.botWait()
        temperature = self.browser.find_element(By.XPATH, "//*[@id='temperatureContentField']").text
        Edges = re.findall(r'\d+', temperature)
        if temperature[3] == '-':
            Edges[0] = '-'+Edges[0]

        average = (int(Edges[0])+int(Edges[1]))/2
        self.mainPlanetState.set('temperature', average)

    def getInfoPlanetPosition(self):
        self.setScope('overview')
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[@id='positionContentField']/a")))
        positionString = self.browser.find_element(By.XPATH, "//*[@id='positionContentField']/a").text

        numbers = re.findall(r'\d+', positionString)
        self.mainPlanetState.set('Galaxy', numbers[0])
        self.mainPlanetState.set('Star', numbers[1])
        self.mainPlanetState.set('Planet', numbers[2])

    def logout(self):
        self.setScope('logout')

    def getInfoPlanetNumber(self):
        self.setScope('overview')

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[@id='countColonies']/p/span")))
        string = self.browser.find_element(By.XPATH, "//*[@id='countColonies']/p/span").text
        planetNumber = string[2]
        self.planetNumber = planetNumber

    def launchBrowser(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
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
        :param page: string: on of these: overview, resources, station, traderOverwie, research, shipyard, defense,
        fleet, galaxy, highscore
        :return: Nothing
        """
        currentURL = self.browser.current_url
        uninumber = currentURL[9] + currentURL[10] + currentURL[11]

        if self.current_scope == page:
            return
        if page == 'fleet':
            self.browser.get("https://s"+uninumber+"-pl.ogame.gameforge.com/game/index.php?page=fleet1")
        else:
            self.browser.get("https://s"+uninumber+"-pl.ogame.gameforge.com/game/index.php?page=" + page)
        self.current_scope = page

    def build(self, *args):
        thing = args[0]

        if len(args) == 1:

            if thing in self._resources:
                self.setScope('resources')
                selection = "//a[@ref='" + self._resources[thing] + "']"
                btnToClick = self.browser.find_element(By.XPATH, selection)
                btnToClick.click()
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content']/div[2]/a")))
                build = self.browser.find_element(By.XPATH, "//*[@id='content']/div[2]/a")
                build.click()
            if thing in self._station:
                self.setScope('station')
                selection = "//a[@ref='" + self._station[thing] + "']"
                btnToClick = self.browser.find_element(By.XPATH, selection)
                btnToClick.click()
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content'']/span")))
                build = self.browser.find_element(By.XPATH, "//*[@id='content']/div[2]/a")
                build.click()
            if thing in self._research:
                self.setScope('research')
                selection = "//a[@ref='" + self._research[thing] + "']"
                btnToClick = self.browser.find_element(By.XPATH, selection)
                btnToClick.click()
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content']/span")))
                build = self.browser.find_element(By.XPATH, "//*[@id='content']/div[2]/a")
                build.click()

        if len(args) == 2:
            number = args[1]
            if thing in self._fleet:
                self.setScope('shipyard')
                selection = "//a[@ref='" + self._fleet[thing] + "']"
                btnToClick = self.browser.find_element(By.XPATH, selection)
                btnToClick.click()
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located((By.ID, "number")))
                numberField = self.browser.find_element_by_id('number')
                numberField.send_keys(number)
                build = self.browser.find_element(By.XPATH, "//*[@id='content']/div[3]/a/span")
                build.click()
            if thing in self._defense:
                self.setScope('defense')
                selection = "//a[@ref='" + self._defense[thing] + "']"
                btnToClick = self.browser.find_element(By.XPATH, selection)
                btnToClick.click()
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located((By.ID, "number")))
                numberField = self.browser.find_element_by_id('number')
                numberField.send_keys(number)
                build = self.browser.find_element(By.XPATH, "//*[@id='content']/div[3]/a/span")
                build.click()

    def buildCancel(self, somethingToCancel):
        if somethingToCancel in self._resources:
            self.setScope('resources')

            WebDriverWait(self.browser, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//*[@id='inhalt']/div[5]/div[2]/table/tbody/tr[2]/td[1]/div/a[2]/img")))

            cancel = self.browser.find_element_by_xpath("//*[@id='inhalt']/div[5]/div[2]/table/tbody/tr[2]/td[1]/div/a[2]/img")
            cancel.click()

        if somethingToCancel in self._station:
            self.setScope('resources')

            WebDriverWait(self.browser, 10).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//*[@id='inhalt']/div[5]/div[2]/table/tbody/tr[2]/td[1]/div/a[2]/img")))

            cancel = self.browser.find_element_by_xpath(
                "//*[@id='inhalt']/div[5]/div[2]/table/tbody/tr[2]/td[1]/div/a[2]/img")
            cancel.click()

        if somethingToCancel in self._research:
            self.setScope('research')
            selection = "//a[@ref='" + self._research[somethingToCancel] + "']"
            btnToClick = self.browser.find_element(By.XPATH, selection)
            btnToClick.click()
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content']/span")))
            cancel = self.browser.find_element_by_class_name("tooltip abort_link js_hideTipOnMobile")
            cancel.click()

        if somethingToCancel in self._fleet:
            self.setScope('shipyard')
            selection = "//a[@ref='" + self._fleet[somethingToCancel] + "']"
            btnToClick = self.browser.find_element(By.XPATH, selection)
            btnToClick.click()
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_all_elements_located((By.ID, "number")))
            cancel = self.browser.find_element_by_class_name("tooltip abort_link js_hideTipOnMobile")
            cancel.click()

        if somethingToCancel in self._defense:
            self.setScope('defense')
            selection = "//a[@ref='" + self._defense[somethingToCancel] + "']"
            btnToClick = self.browser.find_element(By.XPATH, selection)
            btnToClick.click()
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_all_elements_located((By.ID, "number")))
            cancel = self.browser.find_element_by_class_name("tooltip abort_link js_hideTipOnMobile")
            cancel.click()

    def setSpyProbeCount(self, number):
        self.setScope('preferences')
        overall = self.browser.find_element(By.XPATH, '//*[@id="tabs-pref"]/li[2]')
        overall.click()
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[@id='two']/div[2]/div/div/input")))
        numberField = self.browser.find_element(By.XPATH, '//*[@id="two"]/div[2]/div/div/input')
        numberField.send_keys(number)
        accept = self.browser.find_element_by_xpath("//*[@id='prefs']/div[1]/div[5]/input")
        accept.click()

        # TODO
