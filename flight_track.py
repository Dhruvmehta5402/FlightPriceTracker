from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import smtplib

URL = 'https://www.kayak.co.in/flights/CCU-ORD/2021-08-17/2021-12-20?sort=bestflight_a'
PRICE_LIMIT = 80000
SENDER_EMAIL = ''
SENDER_PASSWORD = ''
RECEIVER_EMAIL = 'dhruvmehtakolkata@gmail.com'
CHECKING_INTERVAL = 60
NUMBER_OF_CHECKS = 2

for i in range(NUMBER_OF_CHECKS):
    driver = webdriver.Chrome()
    driver.get(URL)
    time.sleep(25)
    content = driver.page_source
    soup = BeautifulSoup(content)

    for span in soup.findAll('span', attrs={'class':'js-label js-price _itL _ibU _ibV _idj _kKW'}):
        price = span.text[-6:]
        print(price)

    price = price.replace(',', '')

    body = f"Hello! The price is now within your range: {price}. Buy it quick before it rises again."
    message = 'Subject: {}\n\n{}'.format('Flight Price', body)

    if int(price) > 9999 and int(price) <= PRICE_LIMIT:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(SENDER_EMAIL, SENDER_PASSWORD)
        print(message)
        s.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)
        print('Email has been sent')
        s.quit()

    driver.quit()
    time.sleep(CHECKING_INTERVAL)