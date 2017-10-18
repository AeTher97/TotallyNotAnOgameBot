from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote import webelement
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

        self._fleet = {'LightFighter': '204',
                       'HeavyFighter': '205',
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

        self._missions = {'Expedition':'15','Colonize':'7','Recycle':'8','Transport':'3','Station':'4',
                          'Spy':'6','Stop':'5','Attack':'1','AllyAttack':'2','Destroy':'9'}

        self.current_scope = ""
        self.browser = None
        self.mainPlanetState = PlanetState()
        self.planetNumber = 0
        self.airborneFleets = 0

    def getInfoResources(self):
        self.setScope('overview')
        metal = self.browser.find_element_by_id('resources_metal').text
        crystal = self.browser.find_element_by_id('resources_crystal').text
        deuter = self.browser.find_element_by_id('resources_deuterium').text
        energy = self.browser.find_element_by_id('resources_energy').text

        self.mainPlanetState.set("metal", int(metal.replace('.', '')))
        self.mainPlanetState.set("crystal", int(crystal.replace('.', '')))
        self.mainPlanetState.set("deuter", int(deuter.replace('.', '')))
        self.mainPlanetState.set("energy", int(energy.replace('.', '')))

    def getInfoBuildings(self):
        self.setScope('resources')

        for building in self._resources:
            try:
                if building != 'SolarSatellite':
                    selection = "//a[@ref='" + self._resources[building] + "']"
                    btnToClick = self.browser.find_element(By.XPATH, selection)
                    btnToClick.click()
                    WebDriverWait(self.browser, 10).until(
                        EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content']/div[2]/a")))

                    level = int(re.search(r'\d+', self.browser.find_element_by_xpath(
                        "//*[@id='content']/span").text).group())
                    self.mainPlanetState.set(building, level)
            except:
                overlay = self.browser.find_element(By.XPATH,'//*[@id="details'+str(self._resources[building])+'"]')
                overlay.click()
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content']/div[2]/a")))

                level = int(re.search(r'\d+', self.browser.find_element_by_xpath(
                    "//*[@id='content']/span").text).group())
                self.mainPlanetState.set(building, level)

        self.setScope('station')
        for building in self._station:
            try:
                selection = "//a[@ref='" + self._station[building] + "']"
                btnToClick = self.browser.find_element(By.XPATH, selection)
                btnToClick.click()
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content']/div[2]/a/span")))
                level = int(re.search(r'\d+', self.browser.find_element_by_xpath("//*[@id='content']/span").text).group())
                self.mainPlanetState.set(building, level)
            except:
                overlay = self.browser.find_element(By.XPATH,'//*[@id="details' + str(self._station[building]) + '"]')
                overlay.click()
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content']/div[2]/a")))

                level = int(re.search(r'\d+', self.browser.find_element_by_xpath(
                    "//*[@id='content']/span").text).group())
                self.mainPlanetState.set(building, level)


    def getInfoTechnology(self):
        self.setScope('research')

        for research in self._research:
            try:
                selection = "//a[@ref='" + self._research[research] + "']"
                btnToClick = self.browser.find_element(By.XPATH, selection)
                btnToClick.click()
                WebDriverWait(self.browser, 10).until(
                     EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content']/div[2]/a")))

                level = int(re.search(r'\d+', self.browser.find_element_by_xpath("//*[@id='content']/span").text).group())
                self.mainPlanetState.set(research, level)
            except:
                overlay = self.browser.find_element(By.XPATH,'//*[@id="details' + str(self._research[research]) + '"]')
                overlay.click()
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content']/div[2]/a")))

                level = int(re.search(r'\d+', self.browser.find_element_by_xpath(
                    "//*[@id='content']/span").text).group())
                self.mainPlanetState.set(research, level)

    def getInfoFleetSize(self):
        self.setScope('shipyard')


        for ship in self._fleet:
            try:
                selection = "//a[@ref='" + self._fleet[ship] + "']"
                btnToClick = self.browser.find_element(By.XPATH, selection)
                btnToClick.click()
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located((By.ID, "number")))

                number = int(re.search(r'\d+', self.browser.find_element_by_xpath("//*[@id='content']/span").text).group())
                self.mainPlanetState.set(ship, number)
            except:
                overlay = self.browser.find_element(By.XPATH, '//*[@id="details' + str(self._fleet[ship]) + '"]')
                overlay.click()
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located((By.ID, "number")))

                level = int(re.search(r'\d+', self.browser.find_element_by_xpath(
                    "//*[@id='content']/span").text).group())
                self.mainPlanetState.set(ship, level)


    def getInfoDefenses(self):
        self.setScope('defense')

        for defense in self._defense:
            try:
                if defense != 'SmallPlanetaryShield' and defense != 'LargePlanetaryShield':
                    selection = "//a[@ref='" + self._defense[defense] + "']"
                    btnToClick = self.browser.find_element(By.XPATH, selection)
                    btnToClick.click()
                    WebDriverWait(self.browser, 10).until(
                        EC.presence_of_all_elements_located((By.ID, "number")))

                    number = int(re.search(r'\d+', self.browser.find_element_by_xpath("//*[@id='content']/span").text).group())
                    self.mainPlanetState.set(defense, number)
                else:
                    selection = "//a[@ref='" + self._defense[defense] + "']"
                    btnToClick = self.browser.find_element(By.XPATH, selection)
                    btnToClick.click()
                    WebDriverWait(self.browser, 10).until(
                        EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content']/span")))

                    number = int(
                        re.search(r'\d+', self.browser.find_element_by_xpath("//*[@id='content']/span").text).group())
                    self.mainPlanetState.set(defense, number)
            except:
                overlay = self.browser.find_element(By.XPATH, '//*[@id="details' + str(self._defense[defense]) + '"]')
                overlay.click()
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content']/span")))

                level = int(re.search(r'\d+', self.browser.find_element_by_xpath(
                    "//*[@id='content']/span").text).group())
                self.mainPlanetState.set(defense, level)


    def getInfoSizeOfPlanet(self):
        self.setScope('overview')
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[@id='diameterContentField']/span[2]")))
        planetSize = self.browser.find_element(By.XPATH, "//*[@id='diameterContentField']/span[2]").text
        self.mainPlanetState.set('PlanetSize', int(planetSize.replace('.', '')))

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

    def getInfoAttacks(self):
        """

        :return: return PlanetState objcets of planet being attacked if no planets are being attacked returns 0
        """
        plantesUnderAttack = []
        try:

            WebDriverWait(self.browser, 1).until(
                 EC.presence_of_all_elements_located((By.XPATH, "//*[@id='eventboxFilled']/p/span")))
            string = self.browser.find_element(By.XPATH, '//*[@id="eventboxFilled"]/p').text

            if string.find('wrogi') != -1 and string.find('wrogie') != -1:
                print('lol')
                number = re.findall(r'\d+', string)
                print('warning '+str(number[2])+'attacks')
                expand = self.browser.find_element_by_xpath('//*[@id="js_eventDetailsClosed"]')
                self.botWait()
                listTimesAttacks = self.browser.find_elenets_by_class_name('//*[@id="counter-eventlist-12767572"]').text
                listTimesOwnFleets = self.browser.find_elenets_by_class_name('countDown friendly textBeefy').text
                listCoordinates = self.browser.find_elenets_by_class_name('//*[@id="eventContent"]/tbody/tr[1]/td[9]').text
                listsCombined = []
                j=0

                attacksWithCords = {}
                for i in range(0,len(listTimesAttacks)+len(listTimesOwnFleets)):
                    if j < len(listTimesAttacks):
                        listsCombined[i]=listTimesAttacks[i]
                        j+=1
                    else:
                        listsCombined[i]=listTimesOwnFleets[i-j]
                listsCombined.sort()
                j=0
                for time in listsCombined:
                    if listsCombined[i]==listTimesAttacks[j]:
                        attacksWithCords[str(listsCombined[i])] = str(listCoordinates[i])
                        j+=1

                planet = PlanetState()
                for element in attacksWithCords:
                    numbers = re.findall(r'\d+', attacksWithCords[element])
                    planet.set('Galaxy', int(numbers[0].replace('.', '')))
                    planet.set('Star', int(numbers[1].replace('.', '')))
                    planet.set('Planet', int(numbers[2].replace('.', '')))
                    plantesUnderAttack.append(planet)
                    print('found planet under attack ['+str(numbers[0])+':'+str(numbers[1])+':'+str(number[2])+']')

                return plantesUnderAttack
        except:
            print('no attacks')
            return 0


    def getInfoPlanetPosition(self):
        self.setScope('overview')
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[@id='positionContentField']/a")))
        positionString = self.browser.find_element(By.XPATH, "//*[@id='positionContentField']/a").text

        numbers = re.findall(r'\d+', positionString)
        self.mainPlanetState.set('Galaxy', int(numbers[0].replace('.', '')))
        self.mainPlanetState.set('Star', int(numbers[1].replace('.', '')))
        self.mainPlanetState.set('Planet', int(numbers[2].replace('.', '')))

    def getInfoFleets(self):
        """

        :return: returns number of airborne fleets
        """

        try:
            WebDriverWait(self.browser, 1).until(
                 EC.presence_of_all_elements_located((By.XPATH, "//*[@id='eventboxFilled']/p/span")))
            string = self.browser.find_element(By.XPATH, '//*[@id="eventboxFilled"]/p').text

            number = re.findall(r'\d+', string)
            self.airborneFleets = int(number[1])
            return self.airborneFleets
        except:
            print('no fleets airborne')
            self.airborneFleets = 0
            return 0



    def logout(self):
        self.setScope('logout')

    def getInfoPlanetNumber(self):
        self.setScope('overview')

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[@id='countColonies']/p/span")))
        string = self.browser.find_element(By.XPATH, "//*[@id='countColonies']/p/span").text
        planetNumber = string[2]
        self.planetNumber = planetNumber

    def getInfoAll(self):
        """
        call every getInfor function for main planet
        :return: Nothing
        """
        self.getInfoPlanetNumber()
        self.getInfoFleets()
        self.getInfoPlanetTemperature()
        self.getInfoResources()
        self.getInfoSizeOfPlanet()
        self.getInfoBuildings()
        self.getInfoDefenses()
        self.getInfoFleetSize()
        """
        self.getInfoPlanetPosition()
        """

        self.getInfoTechnology()

    def launchBrowser(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.get(('https://pl.ogame.gameforge.com/'))

    def login(self, login, password, universe):
        commercialCloseButton = self.browser.find_element(By.XPATH, "//a[@href='javascript:;']")
        commercialCloseButton.click()
        LoggedIn=0
        FailCounter=0
        while LoggedIn==0:
            try:
                LoginWindowOpen = self.browser.find_element_by_id('loginBtn')
                LoginWindowOpen.click()
            except:
                print('login window extended')
            usernameField = self.browser.find_element_by_id('usernameLogin')
            passwordField = self.browser.find_element_by_id('passwordLogin')
            serverField = self.browser.find_element_by_id('serverLogin')
            loginButton = self.browser.find_element_by_id('loginSubmit')



            try:
                for i in login:
                    usernameField.send_keys(i)
                for i in password:
                    passwordField.send_keys(i)
                serverField.send_keys(universe)
                loginButton.click()
            except:
                print('failed again')
            try:
                self.browser.find_element_by_xpath('//*[@id="logoLink"]')
                LoggedIn=1
            except:
                print('failed to log in')
            if FailCounter=='5':
                self.browser.get(('https://pl.ogame.gameforge.com/'))

        self.current_scope = "overview"

    def botWait(self, seconds=1):
        time.sleep(seconds)

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
            self.browser.get("https://s"+str(uninumber)+"-pl.ogame.gameforge.com/game/index.php?page=fleet"+str(self.airborneFleets))
        else:
            self.browser.get("https://s"+uninumber+"-pl.ogame.gameforge.com/game/index.php?page=" + page)
        self.current_scope = page

    def build(self, *args):
        """

        :param args:
        :return:
        :except: cannot build if cannot build
        """
        thing = args[0]

        if len(args) == 1:

            if thing in self._resources:
                self.setScope('resources')
                selection = "//a[@ref='" + self._resources[thing] + "']"
                btnToClick = self.browser.find_element(By.XPATH, selection)
                try:
                    btnToClick.click()
                except:
                    raise Exception('cannot build')
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content']/div[2]/a")))
                build = self.browser.find_element(By.XPATH, "//*[@id='content']/div[2]/a")
                build.click()
                return
            if thing in self._station:
                self.setScope('station')
                selection = "//a[@ref='" + self._station[thing] + "']"
                btnToClick = self.browser.find_element(By.XPATH, selection)
                try:
                    btnToClick.click()
                except:
                    raise Exception('cannot build')
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content']/span")))
                build = self.browser.find_element(By.XPATH, "//*[@id='content']/div[2]/a")
                build.click()
                return
            if thing in self._research:
                self.setScope('research')
                selection = "//a[@ref='" + self._research[thing] + "']"
                btnToClick = self.browser.find_element(By.XPATH, selection)
                try:
                    btnToClick.click()
                except:
                    raise Exception('cannot build')
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//*[@id='content']/span")))
                build = self.browser.find_element(By.XPATH, "//*[@id='content']/div[2]/a")
                build.click()
                return

        if len(args) == 2:
            number = args[1]
            if thing in self._fleet:
                self.setScope('shipyard')
                selection = "//a[@ref='" + self._fleet[thing] + "']"
                btnToClick = self.browser.find_element(By.XPATH, selection)
                try:
                    btnToClick.click()
                except:
                    raise Exception('cannot build')

                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located((By.ID, "number")))
                numberField = self.browser.find_element_by_id('number')
                try:
                    numberField.send_keys(number)
                except:
                    print('cant choose any number')
                build = self.browser.find_element(By.XPATH, "//*[@id='content']/div[3]/a/span")
                build.click()
                return
            if thing in self._defense:
                self.setScope('defense')
                selection = "//a[@ref='" + self._defense[thing] + "']"
                btnToClick = self.browser.find_element(By.XPATH, selection)
                try:
                    btnToClick.click()
                except:
                    raise Exception('cannot build')
                WebDriverWait(self.browser, 10).until(
                    EC.presence_of_all_elements_located((By.ID, "number")))
                numberField = self.browser.find_element_by_id('number')
                try:
                    numberField.send_keys(number)
                except:
                    print('can choose number')
                build = self.browser.find_element(By.XPATH, "//*[@id='content']/div[3]/a/span")
                build.click()
                return





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

    def setResourcesDigginRater(self,resource,rate):
        self.setScope('resourceSettings')
        if resource=='Metal':
            value = self.browser.find_element_by_xpath('//*[@id="inhalt"]/div[2]/div[2]/form/table/tbody/tr[4]/td[7]/span/a')
            button = self.browser.find_element_by_xpath('//*[@id="factor"]/div/div/span[2]/input')
            value.send_keys(rate)
            button.click()
        if resource=='Crystal':
            value = self.browser.find_element_by_xpath('//*[@id="inhalt"]/div[2]/div[2]/form/table/tbody/tr[5]/td[7]/span/a')
            button = self.browser.find_element_by_xpath('//*[@id="factor"]/div/div/span[2]/input')
            button.click()
        if resource=='Deuter':
            velue = self.browser.find_element_by_xpath('//*[@id="inhalt"]/div[2]/div[2]/form/table/tbody/tr[6]/td[7]/span/a')
            button = self.browser.find_element_by_xpath('//*[@id="factor"]/div/div/span[2]/input')
            button.click()

    def sendFleet(self,fleet,target):
        self.setScope('fleet')
        for attribute in fleet.attributes:
            if fleet.get(attribute) != 0 and attribute!='Mission' and attribute!= 'Speed':
                field = self.browser.find_element_by_id('ship_'+str(self._fleet[attribute]))
                field.send_keys(fleet.get(attribute))
        self.botWait()

        next = self.browser.find_element_by_xpath('//*[@id="continue"]/span')
        try:
            next.click()
        except:
            next.click()

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="speedLinks"]/a[1]')))

        starField = self.browser.find_element_by_xpath('//*[@id="system"]')
        planetField = self.browser.find_element_by_xpath('//*[@id="position"]')

        self.browser.execute_script(
            "document.getElementById('galaxy').value = '"+str(target.get('Galaxy'))+"';")
        starField.send_keys(str(target.get('Star')))
        planetField.send_keys(str(target.get('Planet')))

        speed = self.browser.find_element_by_xpath('//*[@id="speedLinks"]/a['+str(fleet.get('Speed')/10)+']')
        speed.click()

        next = self.browser.find_element_by_xpath('//*[@id="continue"]')
        next.click()

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="roundup"]/ul/li[2]/span')))

        mission = self.browser.find_element_by_id('missionButton'+str(self._missions[fleet.get('Mission')]))
        mission.click()

        if fleet.get('Mission') == 'Transport':
            MetalField = self.browser.find_element_by_xpath('//*[@id="metal"]')
            CrystalField = self.browser.find_element_by_xpath('//*[@id="crystal"]')
            DeuterField = self.browser.find_element_by_xpath('//*[@id="deuterium"]')
            MetalField.send_keys(fleet.get('Metal'))
            CrystalField.send_keys(fleet.get('Crystal'))
            DeuterField.send_keys(fleet.get('Deuter'))

        next = self.browser.find_element_by_xpath('//*[@id="start"]')
        next.click()
        self.airborneFleets = self.airborneFleets+1
        print('finished')

    def changePlanet(self,planet):
        """

        :param planet: number of planet indexing from 1
        :return:
        """
        self.setScope('overview')
        planetbutton = self.browser.find_element_by_xpath("//div[@id='planetList']/div["+str(planet)+"]")
        planetbutton.click()

    def executeOrder(self, order):                                                                                      # TODO execute order on different planets
        """
        :param order: object Order
        :return: Bool: False if couldn't execute order, True otherwise
        """
        if order.action == "gather":
            gathered = False
            while not gathered:
                if(self.mainPlanetState.get("metal") >= order.metal and
                   self.mainPlanetState.get("crystal") >= order.crystal and
                   self.mainPlanetState.get("deuter") >= order.deuter):
                    return True
                else:
                    gathered = False
                    self.botWait(10)
        elif order.action == "build":
            if order.thing in self._fleet or order.thing in self._defense:
                self.build(order.thing, order.lvl)
            else:
                self.build(order.thing)
            return True
        elif order.action == "attack":
            self.sendFleet(order.fleet, order.target)
            return True



    # TODO

