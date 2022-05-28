from selenium import webdriver
from bs4 import BeautifulSoup
import time, csv

START_URL = 'http://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers = ['Name', 'Distance', 'Mass', 'Radius']
    incoming_data = []

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    for tr_tag in soup.find_all('tr'):

        table_data = tr_tag.find_all('td')

        row = [i.text.rstrip() for i in table_data]
        incoming_data.append(row)

    with open('data.csv', 'w', encoding='utf-8') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(incoming_data)

scrape()