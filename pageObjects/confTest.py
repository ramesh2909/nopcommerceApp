import pytest
from selenium import webdriver
@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(options=options)
    options.add_experimental_option("detach", True)
    return driver