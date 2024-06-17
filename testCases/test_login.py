import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from testCases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import logDemo
# from utilities.testlogger import custlogger
class Test_001_Login:

    # baseUrl = "https://admin-demo.nopcommerce.com/"
    # username = 'admin@yourstore.com'
    # password = "admin"
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getPassword()
    logger = logDemo()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):

        self.logger.info("**************** test_001_login *****************")
        self.logger.info("**************** Verifying home page title *****************")
        self.driver = setup
        # self.driver = webdriver.ChromeOptions()
        # self.driver = webdriver.Chrome(options=options)
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option("detach", True)
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**************** home page title test is passed *****************")
        else:
            self.driver.save_screenshot("F:\\software testing material\\videos on software testing\\Python code with harry\\project\\nopcommerce\\screenshots\\test_homePageTitle.png")
            self.driver.close()
            self.logger.error("**************** home page title test is failed *****************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("**************** verifying login test *****************")
        self.driver = setup
        # self.driver = webdriver.ChromeOptions()
        # self.driver = webdriver.Chrome(options=options)
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option("detach", True)
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("**************** login test is passed *****************")
        else:
            self.driver.save_screenshot("F:\\software testing material\\videos on software testing\\Python code with harry\\project\\nopcommerce\\screenshots\\test_login.png")
            self.driver.close()
            self.logger.error("**************** login test is failed *****************")
            assert False
