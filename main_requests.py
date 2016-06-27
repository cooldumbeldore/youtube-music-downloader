import requests
from bs4 import BeautifulSoup
import sys

key_word = sys.argv[1]
youtube_search_url = "https://www.youtube.com/results?search_query=" + key_word

content = requests.get(youtube_search_url).text

soup = BeautifulSoup(content, 'html.parser')

page_body = soup.find_all("div", class_="branded-page-v2-primary-column-content")[1]

results = page_body.find("div", id="results")

ol = results.find("ol", class_="item-section")

a_links = ol.find_all("a", class_="yt-uix-sessionlink")

hrefs = [link['href'] for link in a_links]

video_links = []
for href in hrefs:
	if href[0:6] == "/watch":
		video_links.append(href)

print video_links