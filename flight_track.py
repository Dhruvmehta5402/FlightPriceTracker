from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import smtplib

departure = input("Enter departure location: ")
destination = input("Enter destination: ")
dep_date = input("Enter departure date in YYYY-MM-DD format: ")
arrival_date = input("Enter arrival date in YYYY-MM-DD format: ")
URL = f'https://www.kayak.co.in/flights/{departure}-{destination}/{dep_date}/{arrival_date}?sort=bestflight_a'
PRICE_LIMIT = int(input("Enter price limit: "))
SENDER_EMAIL = input("Enter Sender Email: ")
SENDER_PASSWORD = input("Enter Sender Email Password: ")
RECEIVER_EMAIL = input("Enter Receiver Email: ")
CHECKING_INTERVAL = int(input("Enter Checking Interval in seconds: "))
CHECKING_DURATION = int(input("Enter Checking Duration in seconds: "))
NUMBER_OF_CHECKS = int(CHECKING_DURATION / CHECKING_INTERVAL)

for i in range(NUMBER_OF_CHECKS):
    driver = webdriver.Chrome()
    driver.get(URL)
    time.sleep(30)
    content = driver.page_source
    soup = BeautifulSoup(content)

    for span in soup.findAll('span', attrs={'class':'js-label js-price _itL _ibU _ibV _idj _kKW'}):
        price = ''
        try:
            price_num = (int) (span.text[-8:].replace(',', ''))
            price = span.text[-8:]
        except:
            try:
                price_num = (int) (span.text[-7:].replace(',', ''))
                price = span.text[-7:]
            except:
                try:
                    price_num = (int) (span.text[-6:].replace(',', ''))
                    price = span.text[-6:]
                except:
                    price = span.text[-5:]
        print(price)

    price = price.replace(',', '')
    price = price.strip()
    body = f"Hello! The price is now within your range: {price}. Buy it quick before it rises again."
    message = 'Subject: {}\n\n{}'.format('Flight Price', body)

    if int(price) <= PRICE_LIMIT:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(SENDER_EMAIL, SENDER_PASSWORD)
        print(message)
        s.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)
        print('Email has been sent')
        s.quit()

    driver.quit()
    time.sleep(CHECKING_INTERVAL)