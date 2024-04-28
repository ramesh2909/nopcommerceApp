from utilities.readProperties import ReadConfig


from pytest_metadata.plugin import metadata_key
import pytest
from selenium import webdriver
@pytest.fixture()
def setup(browser):
    if browser == "Chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        options.add_experimental_option("detach", True)
        print("launching chrome browser")

    elif browser == "Firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
        # options.add_experimental_option("detach", True)
        print("launching Firefox browser")

    elif browser == "Edge":
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(options=options)
        options.add_experimental_option("detach", True)
        print("launching Edge browser")
    else:
        driver = webdriver.Edge()

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#############   pytest HTML report  #####################

# it is hook to adding envoirment info to html report
# ''' modifying the table pytest environment'''
def pytest_configure(config):
    config.stash[metadata_key]["Project name1"] = "nop Commerce1"
    config.stash[metadata_key]["Module name1"] = "Customer1"
    config.stash[metadata_key]["Tester1"] = "Pawan1"

    config.stash[metadata_key] = {
        "Project name" : "nop Commerce",
        "Module name" : "Customer",
        "Tester" : "Pawan",
    }






#     it is hook to delete/ modify envoirment info to html report
@pytest.mark.optionalhook

def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)
    metadata.pop("Platform", None)

def pytest_html_report_title(report):
	''' modifying the title of html report'''
	report.title = "Custom Title"




