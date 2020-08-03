from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from datetime import date
import time
from selenium import webdriver
from urllib.error import HTTPError

class Match:
    def __init__(self, t1n, t1i, t2n, t2i, l, s, y, d):
        self.team1Name = t1n
        self.team1Icon = t1i
        self.team2Name = t2n
        self.team2Icon = t2i
        self.League = l
        self.season: s
        self.year = y
        self.date = d

def getBSobject(url):
    try:
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(url,headers=hdr)
        html = urlopen(req)
    except HTTPError as e:
        return e
    try:
        bs = BeautifulSoup(html.read(), 'lxml')
    except AttributeError as e:
        return None
    return bs


if __name__ == "__main__":

    url = "https://lol.gamepedia.com/LCK/2020_Season/Summer_Season"

    # Use Selenium to navigate webpage
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)

    button = driver.find_elements_by_xpath("//div[@class='expand-contract-button']")[1]
    button.click()

    # Get soup object
    soup = BeautifulSoup(driver.page_source, "lxml")

    #Iterate over 10 weeks
    for i in range(1, 11):     

        # Set up the matches to iterate over
        classesToIterate = ["ml-allw ml-w" +str(i) + "ml-row", "ml-allw ml-w" +str(i) + "ml-row matchlist-newday"]

        tr = soup.find_all("tr", class_=classesToIterate)
        temp = tr[1].find_all("span", class_="teamname")
        print(temp)
