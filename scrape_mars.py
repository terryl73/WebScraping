from bs4 import BeautifulSoup
import requests

def scrape

#Find Title
url = 'https://mars.nasa.gov/news/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
result = soup.find_all('div', class_='content_title')
Block1 = result[0]
title = Block1.find('a').text
#RETURN TITLE
print(title)

#Find Paragraph Text
link = Block1.a['href']
url = "https://mars.nasa.gov" + link
print(url)
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
p_result = soup.find_all('p')
for i in range(0,5):
    print(p_result[i])
    print("----------------")
    
news_p = p_result[1].text
#RETURN NEWS_P
print(news_p)

#Find daily image
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
base_url = "https://www.jpl.nasa.gov/"
pic_soup = soup.find('a', class_="button fancybox")
print(pic_soup)
pic_link = pic_soup['data-fancybox-href']
pic_link
featured_image_url = base_url + pic_link
#RETURN FEATURED_IMAGE_URL
browser.visit(featured_image_url)


#Mars Weather Tweet

url = 'https://twitter.com/marswxreport?lang=en'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
mw_tweet = soup.find_all('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
mars_weather = mw_tweet[0].text
#RETURN MARS_WEATHER
mars_weather


#Mars Table

import pandas as pd

url = "https://space-facts.com/mars/"
tables = pd.read_html(url)
df = tables[0]
print(df)
print("------")
html_table = df.to_html()
html_table = html_table.replace('\n', '')
#RETURN HTML_TABLE
html_table

