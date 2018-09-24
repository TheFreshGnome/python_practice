#!/usr/bin/python3

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myUrl = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
uClient = uReq(myUrl)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class":"item-container"}) # each  card

fileName = "graphics card.csv"
f = open(fileName, "w")
headers = "Brand, product_name, shipping\n"
f.write(headers)

for container in containers:
	brand = container.div.div.a.img["title"]
	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text
	shipping = container.findAll("li", {"class":"price-ship"})[0].text.strip()
	f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")

f.close()

	 