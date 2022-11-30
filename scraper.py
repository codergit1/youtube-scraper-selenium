from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# When Chromedriver crashed while importing Selenium, the solution's given below

from selenium.webdriver.chrome.options import Options


def get_driver():

  #Initializing options for chromedriver
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')

  #Configuring Chromedriver
  gchrome_driver = webdriver.Chrome(options=chrome_options)
  return gchrome_driver



def get_videos(driver):
  YT_TRENDING_URL = "https://www.youtube.com/feed/trending"

  VIDEO_DIV_TAG = 'ytd-video-renderer'

  driver.get(YT_TRENDING_URL)
  driver.implicitly_wait(21.4)
  
  print('Getting video div tags')
  vid_tag = driver.find_elements(By.TAG_NAME, VIDEO_DIV_TAG)

  return vid_tag

if __name__ == '__main__':

  print("Creating Chrome Driver")
  driver = get_driver()

  print("Fetching Page")
  video = get_videos(driver)

  print('Page Title: ', driver.title) 
  # driver.quit() when used it found 1 video div tag
  
  print(f'Found {len(video)} video div tags')  #can be printed

  #Title, url, thumbnail_url, channel, views, uploaded, description
  print('Parsing the first video')

  vid = video[0]
  title_tag = vid.find_element(By.ID, 'video-title')

    # print(f'Title: {(title_tag)}')

# Found title by searching with 'video-title' but it's an object therefore use .text
  
  title = title_tag.text

  #EXTRA NOTE: Use 'find_element' not 'find_elements'

  url = title_tag.get_attribute('href')
  print('Title: ', title)
  print('URL: ', url)
