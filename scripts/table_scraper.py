#!/usr/bin/python3
"""
Here I use what I learned from several online tutorials to put the top 100 fortnite players stats 
into a .csv file
"""
import requests
from bs4 import BeautifulSoup

# get the data
data = requests.get('https://fortnitetracker.com/leaderboards')

# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

fileName = "fortnite_top100.csv"
f = open(fileName, "w")
headers = "Rank, Name, Wins, Games_Played\n"
f.write(headers)

#this particular chunk strictly for the above site!
td_list = []
tbody = soup.find('tbody')
for tr in tbody.find_all('tr'):
	rank = tr.find_all('td')[0].text.strip()	
	username = tr.find_all('td')[1].find('a').text.strip()
	wins = tr.find_all('td')[2].text.strip()
	Games_Played = tr.find_all('td')[3].text.strip()
	f.write(rank + "," + username + "," + wins.replace(",", "|") + "," + Games_Played + "\n")
f.close()


