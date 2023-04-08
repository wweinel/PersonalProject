import re
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


# 'scrape' function that takes in the following parameters
#         'url' of website in form "https...pg={}"
#         'startPage' to 'endPage' includes all the pages you want 'scrape' to look through
#         'csvName' name of .csv file to be created or overwritten with data
#         returns pandas dataframe of webpage data       
def scrape(url:str,startPage:int,endPage:int,csvName:str):
     chrome_options = Options()  
     chrome_options.add_argument("--headless") # Opens the browser up in background

     # Columns for data collected through 'scrape' function
     ratings = [] 
     dates = []

     # Looping through every page between startPage-endPage inclusive
     for page_num in range (startPage,(endPage+1)):
          with Chrome(options=chrome_options) as browser:
               page_url = url.format(page_num)
               browser.get(page_url)
               wait = WebDriverWait(browser, 40) # Wait up to 20 seconds for the element to be present
               wait.until(EC.presence_of_element_located((By.ID, 'top-of-reviews')))
               dom = browser.execute_script("return document.documentElement.outerHTML")

          page_soup = BeautifulSoup(dom, 'html.parser')
          good_soup = page_soup.find(id="__render-farm")
          block = good_soup.find(id="top-of-reviews")
          container = block.find_all("div", class_="flex row")

          # Looping through review 'container' to find rating (int of 5) and date (Mon Day, Year)
          for container in container:
               rating = container.find("div", class_="flex-shrink-0 mr2")
               rating = rating.get('aria-label')
               ratings.append(int(rating.split()[1]))
               date = container.find("span", class_="f5 self-start relative kpl-color-text-primary")
               date = date.text.strip()
               dates.append(date)
          
     df = pd.DataFrame({"rating out of 5": ratings, "date": dates}) # Adding columnn headers to dataframe
     df.to_csv("data/" + csvName, index=False) # Writing dataframe to file.csv
     return df

