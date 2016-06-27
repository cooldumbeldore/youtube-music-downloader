from selenium import webdriver

browser = webdriver.FireFox()

url = 'https://www.youtube.com'
search_term = "bla"
enter = webdriver.common.keys.Keys.RETURN

browser.get(url)

search_input = browser.find_element_by_id("masthead-search-term")

search_input.send_keys(search_term)

submit_button = browser.find_element_by_id("search-btn")

submit_button.send_keys(enter)