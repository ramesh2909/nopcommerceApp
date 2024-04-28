import random
import string
import time

import pytest
from selenium.webdriver.common.by import By
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from testCases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import logDemo

class Test_004_SearchCustomerByEmail:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()
    logger = logDemo()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):

        self.logger.info("**************** Test_004_searchCustomerByEmail *****************")
        self.logger.info("**************** Verifying searchCustomerByEmail *****************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**************** login successful *****************")
        self.logger.info("**************** starting searchCustomerByEmail test *****************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("**************** searching Customer By Email id *****************")

        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(2)
        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("**************** Tc SearchCustomerByEmail finished *****************")
