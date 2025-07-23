import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def browser(request):
    options =webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.implicitly_wait(15)
    request.cls.driver = driver
    yield
    driver.quit()