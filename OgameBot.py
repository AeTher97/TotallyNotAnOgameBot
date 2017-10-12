from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class OgameBot:
    def _getInfoResources(self):
        pass

    def _getInfoBuildings(self):
        pass

    def _getInfoTechnology(self):
        pass

    def _getInfoSizeOfPlanet(self):
        pass

    def _getInfoPlanetNumber(self):
        pass

    def _launchBrowser(self):
        self.browser = webdriver.Chrome()
        self.browser.get(('https://pl.ogame.gameforge.com/'))

    def _login(self, login, password, universe):
        commercialCloseButton = self.browser.find_element(By.XPATH,"//a[@href='javascript:;']")
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

        print(login)
        print(password)
        print(universe)
        loginButton.click()

    def _botWait(self):
        time.sleep(1)

    def changeScope(self):
        pass

    # TODO



"""login: michael93509@gmail.com password: oOunv72Pg744nd2d45zo: universe: Uriel"""