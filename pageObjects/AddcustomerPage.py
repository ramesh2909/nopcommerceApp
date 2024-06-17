import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddCustomer:
    linkCustomer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    linkCustomer_menuItem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddNew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdmMaleGender_xpath = "//input[@id='Gender_Male']"
    rdmFemaleGender_xpath = "//input[@id='Gender_Female']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtCustomerRoles_xpath = "//div[@class='input-group-append input-group-required']//ul[@class='select2-selection__rendered']"
    listItemAdministrator_xpath = "//li[contains(text(),'Administrators')]"
    listItemRegistered_xpath = "//li[contains(text(),'Registered')]"
    listItemVendor_xpath = "//li[contains(text(),'Vendors')]"
    listItemGuests_xpath = "//li[contains(text(),'Guests')]"
    listItemClear_xpath = "//span[@title='delete']"
    drpMgrOfVendor_xpath = "//select[@id='VendorId']"
    txtAdminComment_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.linkCustomer_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.linkCustomer_menuItem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.btnAddNew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setClearCustomerRoles(self):
        self.driver.find_element(By.XPATH, self.listItemClear_xpath).click()

    def setCustomerRole(self):
        self.driver.find_element(By.XPATH, self.txtCustomerRoles_xpath).click()
    def setCustomerRoles(self, role):
        if role == "Registered":
            self.listItem = self.driver.find_element(By.XPATH, self.listItemRegistered_xpath)
            # time.sleep(3)
        elif role == "Administrators":
            self.listItem = self.driver.find_element(By.XPATH, self.listItemAdministrator_xpath)
            # time.sleep(3)
        elif role == "Guests":
            self.driver.find_element(By.XPATH, "//span[@title='delete']").click()
            self.listItem = self.driver.find_element(By.XPATH, self.listItemGuests_xpath)
            # time.sleep(3)
        elif role == "Registered":
            self.listItem = self.driver.find_element(By.XPATH, self.listItemRegistered_xpath)
            # time.sleep(3)
        elif role == "Vendors":
            self.listItem = self.driver.find_element(By.XPATH, self.listItemVendor_xpath)
            # time.sleep(3)
        else:
            self.listItem = self.driver.find_element(By.XPATH, self.listItemGuests_xpath)
            # time.sleep(3)
            # self.listItem.click()
            self.driver.execute_script("arguments[0].click();", self.listItem)

    def setManegerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpMgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.rdmMaleGender_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.rdmFemaleGender_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdmMaleGender_xpath).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)
    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminComment_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()

