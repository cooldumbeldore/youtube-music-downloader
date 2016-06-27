import requests
from bs4 import BeautifulSoup
import sys

# youtube_url = "https://www.youtube.com/watch?v=TNN9MnbhqKY"

def find_links(youtube_url):
	content = requests.get(youtube_url).text

	soup = BeautifulSoup(content, 'html.parser')

	a_links = soup.find_all("a", class_="yt-uix-sessionlink")

	hrefs = [link['href'] for link in a_links]

	video_links = []
	for href in hrefs:
		if href[0:6] == "/watch":
			video_links.append(href)

	return video_links

def find_links_recursivly(base_url, depth):
	if depth == 0:
		return []

	urls = find_links(base_url)
	links = urls
	for url in urls:
		links += find_links_recursivly(url, depth - 1)

	return links