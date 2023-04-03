from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def reviewCount(url:str):

    chrome_options = Options()  
    chrome_options.add_argument("--headless") # Open the browser up in background
    with Chrome(options=chrome_options) as driver:
        page_url = url.format(1)
        driver.get(page_url)
        wait = WebDriverWait(driver, 20) # Wait up to 20 seconds for the element to be present
        wait.until(EC.presence_of_element_located((By.ID, 'top-of-reviews')))
        dom = driver.page_source
        page_soup = BeautifulSoup(dom, 'html.parser')
        reviews = int(page_soup.find("div", class_="mw8 center bg-white flex flex-row items-center justify-center mt0 mb3").text.strip().split()[-1])

        driver.quit() # Close the Chrome driver

    return reviews