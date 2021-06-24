from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import smtplib


driver = webdriver.Chrome()
driver.get('https://www.kayak.co.in/flights/CCU-ORD/2021-08-17/2021-12-20?sort=bestflight_a')
time.sleep(25)
content = driver.page_source
soup = BeautifulSoup(content)

for span in soup.findAll('span', attrs={'class':'js-label js-price _itL _ibU _ibV _idj _kKW'}):
    price = span.text[-6:]
    print(price)

price = price.replace(',', '')

if int(price) > 9999 and int(price) <= 80000:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("", "")
    #price_code = price.encode('utf-8')
    message = f"Hello the price is {price}"
    print(message)
    s.sendmail("", "dhruvmehtakolkata@gmail.com", message)
    print('Email has been sent')