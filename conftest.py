import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from subprocess import getoutput
from selenium.webdriver.chrome.options import Options as OptionsChrome

# this code for running snap Firefox, cos I use Ubuntu snap store!!!
options = Options()
options.binary_location = getoutput("find /snap/firefox -name firefox").split("\n")[-1]


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox"),
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en ,en_US ,es")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options_chrome = OptionsChrome()
        options_chrome.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options_chrome)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(service=Service(
            executable_path=getoutput(
                "find /snap/firefox -name geckodriver"
            ).split("\n")[-1]
        ), options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
