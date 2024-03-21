# from selenium import webdriver

# PATH = "/Users/matheus/Downloads/chromedriver-mac-x64/chromedriver"
# driver = webdriver.Chrome(PATH)

# driver.get("https://google.com")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# Set the path to the Chrome driver executable using an environment variable
os.environ["PATH"] += ":/Applications/chromedriver"

# Create Chrome WebDriver options
options = Options()

# Add any desired options here, such as headless mode
options.add_argument("--headless")  # Example: Run Chrome in headless mode

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Safari(options=options)
# driver = webdriver.Chrome(PATH)

driver.get("https://www.apple.com")

driver.quit()