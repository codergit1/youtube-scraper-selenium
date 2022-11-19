from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# When Chromedriver crashed when importing Selenium, the solution's given below

from selenium.webdriver.chrome.options import Options

def get_driver():

  #Initializing options for chromedriver
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  
  #Configuring Chromedriver
  gchrome_driver = webdriver.Chrome(options=chrome_options)
  return gchrome_driver

if __name__ == '__main__':
  
  YT_TRENDING_URL = "https://www.youtube.com/feed/trending"

  print("Creating Chrome Driver")
  driver = get_driver()

  print("Fetching Page")
  driver.get(YT_TRENDING_URL)

  print('Page Title: ', driver.title)