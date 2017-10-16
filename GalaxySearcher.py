from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from planetState import PlanetState
from selenium.webdriver.common.action_chains import ActionChains
from OgameBot import OgameBot
import time
import re

class GalaxySearcher():
    def __init__(self, OgameBot):
        self.browser = OgameBot.browser
        self.bot = OgameBot
        self.targetList = []

    def scanGalaxy(self,radius,startingPlanet):
        self.bot.setScope('galaxy')
        WebDriverWait(self.browser,10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[@id='colonized']")))
        times = 0
        while times <radius:
            self.GoBack()
            times = times+1

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
                            print('zapisuje')
                            planet.set('Galaxy',startingPlanet.get('Galaxy'))
                            planet.set('Star',startingPlanet.get('Star')+j)
                            planet.set('Planet', i)
                            self.targetList.append(planet)
                except:
                    print('failed to find a planet')
                    i = i+1

            self.GoForth()

    def printList(self):
        for element in self.targetList:
            print(element)

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


