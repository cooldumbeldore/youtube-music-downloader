import requests
from bs4 import BeautifulSoup
import sys

youtube_url = "https://www.youtube.com/watch?v=TNN9MnbhqKY"

content = requests.get(youtube_url).text

soup = BeautifulSoup(content, 'html.parser')

a_links = soup.find_all("a", class_="yt-uix-sessionlink")

hrefs = [link['href'] for link in a_links]

video_links = []
for href in hrefs:
	if href[0:6] == "/watch":
		video_links.append(href)

print video_links

