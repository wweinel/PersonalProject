from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.creditkarma.com/reviews/personal-loan/single/id/upstart-personal-loans?pg=1433"
chrome_options = Options()  
chrome_options.add_argument("--headless") # Opens the browser up in background

with Chrome(options=chrome_options) as browser:
     browser.get(url)
     wait = WebDriverWait(browser, 5) # Wait up to 10 seconds for the element to be present
     dom = browser.execute_script("return document.documentElement.outerHTML")


page_soup = BeautifulSoup(dom, 'html.parser')
containers = page_soup.findAll("div",{"class":"center pa3"})
print(containers)
