import os
import sys
import time

import pytest
from selenium import webdriver


class Test_LoginFlow:
    driver = None

    @pytest.yield_fixture()
    def startup(self):
        self.invoke_browser(self)
        yield
        self.close_browser(self)

    @staticmethod
    def invoke_browser(self):
        environment = "Onpremise"

        if environment == "cloud":
            options = webdriver.ChromeOptions()
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--ignore-ssl-errors")
            options.add_experimental_option("detach", True)
            self.driver = webdriver.Remote(command_executor="192.168.200.126",
                                           desired_capabilities={'browserName': 'chrome',
                                                                 'javascriptEnabled': True})
        else:
            options = webdriver.ChromeOptions()
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--ignore-ssl-errors")
            options.add_experimental_option("detach", True)
            self.driver = webdriver.Chrome(options=options,
                                           executable_path="../Browser_Drivers/OSX/chromedriver")
        time.sleep(5)
        self.driver.maximize_window()
        self.driver.get("http://192.168.200.197:31294/Login/Index")

    @staticmethod
    def close_browser(self):
        self.driver.close()

    def test_LoginFlow(self, startup):
        self.driver.find_element_by_xpath("//input[@id='Username']").send_keys("cubusdemo")
        self.driver.find_element_by_xpath("//input[@id='Password']").send_keys("@Cu2010bus")
        self.driver.find_element_by_xpath("//body/main/form/div[@class='loginContainer']/input[1]").click()
        self.driver.find_element_by_xpath("//img[@id='Logout']").click()


