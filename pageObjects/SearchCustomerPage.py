from selenium.webdriver.common.by import By
class SearchCustomer:
    txtEmailId_xpath = "//input[@id='SearchEmail']"
    txtFirstName_xpath = "//input[@id='SearchFirstName']"
    txtLastName_xpath = "//input[@id='SearchLastName']"
    btnSearch_xpath = "//button[@id='search-customers']"
    tblSearchResult_xpath = "//div[@class='dataTables_scroll']"
    table_xpath = "//*[@id='customers-grid_wrapper']/div[1]/div/div"
    tableRows_xpath = "//*[@id='customers-grid']/tbody/tr"
    tableColumns_xpath = "//*[@id='customers-grid']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmailId_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtEmailId_xpath).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def getNoColumn(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//*[@id='customers-grid']/tbody/tr/td[2]").text

            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, name):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            Name = table.find_element(By.XPATH, "//*[@id='customers-grid']/tbody/tr/td[3]").text

            if Name == name:
                flag = True
                break
        return flag