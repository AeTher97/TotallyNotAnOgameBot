from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from OgameBot import OgameBot
import time
import re

class GalaxySearcher(OgameBot):
    def __init__(self, newbrowser):
        self.browser = webdriver.Chrome()
        self.browser = newbrowser

    def refresh(self):
        self.browser.get("www.gazeta.pl")