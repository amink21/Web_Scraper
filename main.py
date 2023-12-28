from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime
import csv
import pandas as pd

URL = 'https://www.amazon.ca/dp/B08MWSBKB6/?coliid=I2Q41YHPJ2U1K7&colid=RCWRJNS5T43F&ref_=list_c_wl_lv_ov_lig_dp_it&th=1&psc=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", "Accept-Encoding": "gzip, deflate, br", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Connection":"close",  "Upgrade-Insecure-Requests": "1"}

pages = requests.get(URL, headers= headers)

soup = BeautifulSoup(pages.content, "html.parser")

title = soup.find(id = "productTitle").get_text()
title = title.strip()
#print(title)

price = soup.find(id = "corePriceDisplay_desktop_feature_div").get_text()
price = price.strip()[1:6]
#print(price)

date = datetime.date.today()
#print(date)

header = ["Product", "Price", "Date"]
data = [title, price, date]

#with open("AmazonScraping.csv", "w", newline="", encoding="utf") as f:
    #writer = csv.writer(f)
    #writer.writerow(header)
    #writer.writerow(data)

df = pd.read_csv(r'C:\Users\Amin\OneDrive\Documents\Web_Scraping\AmazonScraping.csv')
print(df)

with open("AmazonScraping.csv", "a+", newline="", encoding="utf") as f:
    writer = csv.writer(f)
    writer.writerow(data)

def checkPrice():
    URL = 'https://www.amazon.ca/dp/B08MWSBKB6/?coliid=I2Q41YHPJ2U1K7&colid=RCWRJNS5T43F&ref_=list_c_wl_lv_ov_lig_dp_it&th=1&psc=1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", "Accept-Encoding": "gzip, deflate, br", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Connection":"close",  "Upgrade-Insecure-Requests": "1"}

    pages = requests.get(URL, headers= headers)

    soup = BeautifulSoup(pages.content, "html.parser")

    title = soup.find(id = "productTitle").get_text()
    title = title.strip()

    price = soup.find(id = "corePriceDisplay_desktop_feature_div").get_text()
    price = price.strip()[1:6]

    date = datetime.date.today()
    
    header = ["Product", "Price", "Date"]
    data = [title, price, date]

    with open("AmazonScraping.csv", "a+", newline="", encoding="utf") as f:
        writer = csv.writer(f)
        writer.writerow(data)

    if (price > 50):
        sendEmail()

def sendEmail():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login('amin_786@hotmail.com', '#Amin0amin')

    subject = "The price is below on Amazon. GET IT!!"
    body = "Amin, the price is below. It is time to buy it."

    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'amin_786@hotmail.com', 
        message
    )

while(True):
    checkPrice()
    time.sleep(5)
