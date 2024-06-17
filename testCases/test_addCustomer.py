import random
import string
import time
import pytest
from selenium.webdriver.common.by import By
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from testCases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import logDemo

class Test_003_AddCustomer:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()
    logger = logDemo()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self, setup):

        self.logger.info("**************** Test_003_AddCustomer *****************")
        self.logger.info("**************** Verifying home page title *****************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**************** login successful *****************")
        self.logger.info("**************** starting add customer test *****************")
        time.sleep(3)
        self.addcust = AddCustomer(self.driver)
        time.sleep(3)
        self.addcust.clickOnCustomerMenu()
        time.sleep(3)
        self.addcust.clickOnCustomerMenuItem()
        time.sleep(3)
        self.addcust.clickOnAddNew()
        time.sleep(3)

        self.logger.info("**************** providing customer info *****************")

        self.email = random_generator() + "@Gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        # self.addcust.setClearCustomerRoles()
        self.addcust.setCustomerRole()
        self.addcust.setCustomerRoles("Registered")
        self.addcust.setManegerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Pawan")
        self.addcust.setLastName("Kumar")
        self.addcust.setDob("07/05/1985")
        self.addcust.setCompanyName("bussyQA")
        self.addcust.setAdminContent("this is for testing.....")
        time.sleep(3)
        self.addcust.clickOnSave()

        self.logger.info("**************** saving customer info *****************")
        self.logger.info("**************** add customer validation  started *****************")

        self.msg = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissable']").text
        print(self.msg)

        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("**************** add customer test passed ****************")

        else:
            self.driver.save_screenshot("F:\\software testing material\\videos on software testing\\Python code with harry\\project\\nopcommerce\\screenshots\\test_addcustomer_scr.png")
            self.logger.error("**************** add customer test Failed ****************")
            assert True == False

        self.driver.close()
        self.logger.info("**************** ending Test_003_AddCustomer  ****************")

def random_generator(size = 8, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
