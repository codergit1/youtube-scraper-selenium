import pandas as pd
import smtplib

import os

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

# When Chromedriver crashed while importing Selenium, the solution's given below

from selenium.webdriver.chrome.options import Options


def get_driver():

  #Initializing options for chromedriver
  chrome_options = Options()

  chrome_options.page_load_strategy = 'normal'

  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')

  #Configuring Chromedriver
  gchrome_driver = webdriver.Chrome(options=chrome_options)
  return gchrome_driver


def get_videos(driver):

  VIDEO_DIV_TAG = 'ytd-video-renderer'

  YT_TRENDING_URL = "https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl"

  driver.get(YT_TRENDING_URL)
  driver.implicitly_wait(500000)

  print('Getting video div tags')
  vid_tag = driver.find_elements(By.TAG_NAME, VIDEO_DIV_TAG)

  return vid_tag


def parse_video(video):
  
  title_tag = video.find_element(By.ID, 'video-title')
  title = title_tag.text

  #Title & URL
  url = title_tag.get_attribute('href')
  print('Title: ', title)
  print('URL: ', url)

  #Thumbnail & Thumbnail URL
  thumbnail_tag = video.find_element(By.TAG_NAME, 'img')
  thumbnail_url = thumbnail_tag.get_attribute('src')
  print('Thumbnail URL: ', thumbnail_url)

  #Channel
  channel = video.find_element(By.CLASS_NAME, 'ytd-channel-name')
  print('Channel: ', channel.text)

  #Description
  description = video.find_element(By.ID, 'description-text').text
  print('Description: ', description)

  return {
    'Title': title,
    'Url': url,
    'Thumbnail url': thumbnail_url,
    'Channel': channel.text,
    'Description': description
  }

if __name__ == '__main__':

  print("Creating Chrome Driver")
  driver = get_driver()

  print("Fetching Page")
  video = get_videos(driver)

  print('Page Title: ', driver.title)
  
  # driver.quit() when used it found 1 video div tag

  print(f'Found {len(video)} video div tags')

  #Title, url, thumbnail_url, channel, views, uploaded, description
  print('Parsing Top Trending videos')
  vid_data = [parse_video(v) for v in video[:]]
  print(vid_data)

  #PLEASE NOTE: Webdriver loaded fast and exited
  print('Save data to CSV')
  videos_df = pd.DataFrame(vid_data)
  print(videos_df)
  videos_df.to_csv('trending.csv', index = None)
