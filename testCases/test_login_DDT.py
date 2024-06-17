import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from testCases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import logDemo
from utilities import XLUtils

class Test_002_DDT_Login:
    baseUrl = ReadConfig.getApplicationURL()
    # path = r".\\testData\Logindata.xlsx"
    path = r"F:\\software testing material\\videos on software testing\\Python code with harry\\project\\nopcommerce\\testData\\Logindata.xlsx"
    logger = logDemo()

    @pytest.mark.regression
    def test_login_ddt(self, setup):

        self.logger.info("**************** test_002_login_DDT *****************")
        self.logger.info("**************** Verifying login DDT test *****************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, "Sheet1")
        print("Number of Rows in a Excel:", self.rows)
        list_status = []   # empty list variable

        for r in range(2, self.rows+1):
            self.Username = XLUtils.readData(self.path,'Sheet1', r, 1)
            self.Password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.Exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.Username)
            self.lp.setPassword(self.Password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.Exp == "Pass":
                    self.logger.info("**** Passed ****")
                    self.lp.clickLogout()
                    list_status.append("Passed")
                    XLUtils.writeData(self.path, "Sheet1", r, 4, "Passed")
                    XLUtils.fillGreenColor(self.path, "Sheet1", r, 4)
                elif self.Exp == "Fail":
                    self.logger.info("**** Failed ****")
                    self.lp.clickLogout()
                    list_status.append("Failed")
                    XLUtils.writeData(self.path, "Sheet1", r, 4, "Failed")
                    XLUtils.fillRedColor(self.path, "Sheet1", r, 4)

            elif act_title != exp_title:
                if self.Exp == "Pass":
                    self.logger.info("**** Failed ****")
                    list_status.append("Failed")
                    XLUtils.writeData(self.path, "Sheet1", r, 4, "Failed")
                    XLUtils.fillRedColor(self.path, "Sheet1", r, 4)
                elif self.Exp == "Fail":
                    self.logger.info("**** Passed ****")
                    list_status.append("Passed")
                    XLUtils.writeData(self.path, "Sheet1", r, 4, "Passed")
                    XLUtils.fillGreenColor(self.path, "Sheet1", r, 4)

        if "Fail" not in list_status:
            self.logger.info("**** login DDT test passed ****")
            self.driver.close()
            assert True

        else:
            self.logger.info("**** login DDT test Failed ****")
            self.driver.close()
            assert False

        self.logger.info("**** End of login DDT test  ****")
        self.logger.info("****  Completed tc_login_ddt_002 ****")