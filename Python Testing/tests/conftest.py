import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption('browser_name')

    if browser_name == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_options)

    elif browser_name == 'firefox':
        # Invoke Firefox
        firefox_options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=firefox_options)

    elif browser_name == 'edge':
        edge_options = webdriver.EdgeOptions()
        driver = webdriver.Edge(options=edge_options)

    elif browser_name == 'ie':
        ie_options = webdriver.IeOptions()
        driver = webdriver.Ie(options=ie_options)

    elif browser_name == 'safari':
        safari_options = webdriver.SafariOptions()
        driver = webdriver.Safari(options=safari_options)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
