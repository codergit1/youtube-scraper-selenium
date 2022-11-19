import requests

YT_TRENDING_URL = "https://www.youtube.com/feed/trending"

response = requests.get(YT_TRENDING_URL)

print('Status Code:', response.status_code)
"""

print('Output:', response.text[:1000])

with open('trending.html', 'w') as f:
  f.write(response.text)

"""

from bs4 import BeautifulSoup

doc = BeautifulSoup(response.text, 'html.parser')

print('Page Title:', doc.title.text)

# Find all video divs
video_divs = doc.find_all('div', class_='ytd-video-renderer')

print(f'Found {len(video_divs)} videos')
