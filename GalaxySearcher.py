from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from planetState import PlanetState
from selenium.webdriver.common.action_chains import ActionChains
from OgameBot import OgameBot
from fleet import Fleet
import time
import re

class GalaxySearcher():
    def __init__(self, OgameBot):
        self.browser = OgameBot.browser
        self.bot = OgameBot

    def scanGalaxy(self, radius, startingPlanet,sendProbes):
        """

        :param radius: Int
        :param startingPlanet: object PlanetState with coords
        :param sendProbes: Bool
        :return: Nothing
        """
        if radius+startingPlanet.get('Star')>499:
            radius=499-startingPlanet.get('Star')
        if -radius+startingPlanet.get('Star')<1:
            radius=startingPlanet.get('Star')-1

        targetList = []
        self.bot.setScope('galaxy')
        WebDriverWait(self.browser,10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[@id='colonized']")))
        self.GoToSystem(startingPlanet.get('Galaxy'), startingPlanet.get('Star')-radius)

        for j in range (-radius,radius):
            for i in range (1,15):
                try:
                    name = self.browser.find_element(By.XPATH,'//*[@id="galaxytable"]/tbody/tr['+str(i)+']/td[3]').text
                    status = self.browser.find_element(By.XPATH,'//*[@id="galaxytable"]/tbody/tr['+str(i)+']/td[6]/span/span/span').text

                    if name != '':
                        if status == 'i' or status == 'I':
                            planet = PlanetState()

                            print(name)
                            print(status)
                            self.bot.GetInfoGoingFleets()
                            if sendProbes and startingPlanet.get('ComputerTechnology')+1<self.bot.airborneFleets:
                                print('sending a spy')
                                send = self.browser.get_element(By.XPATH,'//*[@id="galaxytable"]/tbody/tr['+str(i)+']/td[8]/span/a[1]/span')
                                self.bot.airborneFleets = self.bot.airborneFleets + 1
                            send.click()
                            planet.set('Galaxy',startingPlanet.get('Galaxy'))
                            planet.set('Star',startingPlanet.get('Star')+j)
                            planet.set('Planet', i)
                            targetList.append(planet)
                except:
                    print('failed to find a planet')
                    i = i+1

            self.GoForth()
        return targetList

    def Colonize(self,radius,startingPlanet):
        """

        :param radius: Int
        :param startingPlanet: object PlanetState with coordinates
        :return: Bool if colonized True if failed to colonize: False
        """

        self.bot.setScope('galaxy')
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[@id='colonized']")))
        if radius+startingPlanet.get('Star')>499:
            radius=499-startingPlanet.get('Star')
        if -radius+startingPlanet.get('Star')<1:
            radius=startingPlanet.get('Star')-1

        counter = 0
        for j in range (-radius,radius):
            self.GoToSystem(startingPlanet.get('Galaxy'), startingPlanet.get('Star')-radius+counter)
            for i in range(1, 15):

                name = self.browser.find_element(By.XPATH, '//*[@id="galaxytable"]/tbody/tr[' + str(i) + ']/td[3]').text
                print(name)
                if name=='' and i>5 and i<10:
                    colonizationFleet = Fleet()
                    planet = PlanetState()
                    colonizationFleet.set('ColonizationShip',1)
                    colonizationFleet.set('Mission','Colonize')
                    planet.set('Galaxy', startingPlanet.get('Galaxy'))
                    planet.set('Star', startingPlanet.get('Star') + counter)
                    planet.set('Planet', i)
                    print('found planet')

                    print('sending fleet')
                    self.bot.sendFleet(colonizationFleet,planet)
                    return True
                else:
                    i = i+1



            self.GoToSystem(startingPlanet.get('Galaxy'), startingPlanet.get('Star') - counter)
            for i in range(1, 15):

                name = self.browser.find_element(By.XPATH, '//*[@id="galaxytable"]/tbody/tr[' + str(i) + ']/td[3]').text
                print(name)
                if i>5 and i<10 and name=='':
                    colonizationFleet = Fleet()
                    planet = PlanetState()
                    colonizationFleet.set('ColonizationShip',1)
                    colonizationFleet.set('Mission','Colonize')
                    planet.set('Galaxy', startingPlanet.get('Galaxy'))
                    planet.set('Star', startingPlanet.get('Star') +radius-counter)
                    planet.set('Planet', i)
                    print('found planet')

                    print('sending fleet')
                    self.bot.sendFleet(colonizationFleet,planet)
                    return True
                else:
                    i = i+1



            counter += 1
        print('failed')
        return False


    def GoBack(self):
        self.bot.setScope('galaxy')
        back = self.browser.find_element(By.XPATH,'//*[@id="galaxyHeader"]/form/span[5]')
        back.click()
        self.bot.botWait()

    def GoForth(self):
        self.bot.setScope('galaxy')
        forth = self.browser.find_element(By.XPATH,'//*[@id="galaxyHeader"]/form/span[6]')
        forth.click()
        self.bot.botWait()

    def GoToSystem(self,Galaxy,Star):
        self.bot.setScope('galaxy')
        Galaxyfield = self.browser.find_element(By.XPATH,'//*[@id="galaxy_input"]')
        Starfield = self.browser.find_element(By.XPATH,'//*[@id="system_input"]')
        Galaxyfield.send_keys(Galaxy)
        Starfield.send_keys(Star)
        button = self.browser.find_element(By.XPATH,'//*[@id="galaxyHeader"]/form/div[1]')
        button.click()


