import re
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.creditkarma.com/reviews/personal-loan/single/id/upstart-personal-loans?pg={}"
chrome_options = Options()  
chrome_options.add_argument("--headless") # Opens the browser up in background

for page_num in range (1,11):
     with Chrome(options=chrome_options) as browser:
          page_url = url.format(page_num)
          browser.get(page_url)
          loaded_sucessfully = 0
          #while(loaded_sucessfully == 0):
          wait = WebDriverWait(browser, 20) # Wait up to 5 seconds for the element to be present
          wait.until(EC.presence_of_element_located((By.ID, 'top-of-reviews')))

          dom = browser.execute_script("return document.documentElement.outerHTML")
          """
          check_soup = BeautifulSoup(dom, 'html.parser')
          loading = check_soup.find("div", {"data-testid": "reviewsLoading"})

          if loading is None:
                    print("Loaded Successfully")
                    loaded_sucessfully = 1
          else:
                    print("Loading failed")
          """

     page_soup = BeautifulSoup(dom, 'html.parser')
     good_soup = page_soup.find(id="__render-farm")

     #containers = page_soup.findAll("div",{"class":"center pa3"})



     block = good_soup.find(id="top-of-reviews")
     container = block.find_all("div", class_="flex row")
     # open a file in write mode
     for container in container:
          rating = container.find("div", class_="flex-shrink-0 mr2")
          rating = rating.get('aria-label')
          date = container.find("span", class_="f5 self-start relative kpl-color-text-primary")
          date = date.text.strip()
          print(rating, " on ", date )

"""
with open('output.txt', 'w') as file:
     #write a string to the file
     
     for container in container:
               file.write(str(container))
"""
