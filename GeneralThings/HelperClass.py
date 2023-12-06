from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class Helper:

    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def getType(self, locatorType):

        locatorType = locatorType.lower()

        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "class_name":
            return By.CLASS_NAME
        elif locatorType == "css_selector":
            return By.CSS_SELECTOR
        elif locatorType == "tag_name":
            return By.TAG_NAME
        elif locatorType == "link_text":
            return By.LINK_TEXT
        elif locatorType == "partial_link_text":
            return By.PARTIAL_LINK_TEXT
        else:
            return "Invalid Locator Type"

    def getElement(self, locator, locatorType):
        element = None

        try:
            element = self.driver.find_element(self.getType(locatorType), locator)
        except:
            print("Invalid locator or Type or element does not exist (atleast till now)")

        return element

    def getElementText(self, locator, locatorType):
        text = ""

        try:
            element = self.getElement(locator, locatorType)
            text = element.text
        except:
            print("Invalid locator or Type or element does not exist/has text (atleast till now)")

        return text

    def getElementAttributeText(self, locator, attribute, locatorType):
        attribute_text = ""

        try:
            element = self.getElement(locator, locatorType)
            attribute_text = element.get_attribute(attribute)
        except:
            print("Invalid locator or Type or Attribute")

        return attribute_text

    def clickElement(self, locator, locatorType):

        try:
            element = self.getElement(locator, locatorType)
            element.click()
        except:
            print("Invalid Locator or Type")


    def getElements(self, locator, locatorType):
        elements = []

        try:
            elements = self.driver.find_elements(self.getType(locatorType), locator)
        except:
            print("Invalid locator or Type or elements do not exist (atleast till now)")

        return elements

    def getListOfElementText(self, locator, locatorType):
        text_list = []

        try:
            elements = self.getElements(locator, locatorType)
            text_list = [element.text for element in elements]
        except:
            print("Invalid Locator or type or Elements do not exist (atleast till now)")

        return text_list

    def getListOfElementAttributeText(self, locator, attribute, locatorType):
        attributeText_list = []

        try:
            elements = self.getElements(locator, locatorType)
            attributeText_list = [element.get_attribute(attribute) for element in elements]
        except:
            print("Invalid locator or type or Attribute or Elements do not exist (atleast till now)")

        return attributeText_list

    def isElementPresent(self, locator, locatorType):
        presence = False

        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                presence = True
        except:
            print("Invalid locator or type or element does not exist (atleast till now)")

        return presence

    def waitForElementToBeVisible(self, locator, locatorType):
        element = None

        wait = WebDriverWait(self.driver, timeout=60, poll_frequency=0.5,
                                    ignored_exceptions=[NoSuchElementException,
                                                        ElementNotVisibleException,
                                                        ElementNotSelectableException])
        try:
            element = wait.until(EC.visibility_of_element_located((self.getType(locatorType), locator)))
        except:
            print("Could not find element (Even after 60 secs)")

        return element
