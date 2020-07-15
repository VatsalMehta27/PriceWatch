import requests
from bs4 import BeautifulSoup
import smtplib
from time import sleep

url = input('Please enter the link: ') 
budget = float(input('Please enter your budget: '))
user_email = input('Please enter your email address: ')
send_to_email = input('Please enter the recipient\'s email address: ')
app_password = input('Please enter the app password: ') # Set up 2-FA and create an app password for your device
title_id = input('Please enter the id of the product name: ')
price_id = input('Please enter the id of the product price: ')

headers = {
    'User-Agent' : # Google "my user agent" to find out your user agent
}


def check_price():    
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id=title_id).get_text().strip()
    price = float(soup.find(id=price_id).get_text().strip().replace(',', ''))

    if price < budget:
        send_email()

    print(title, price)

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(user_email, app_password)
    
    subject = 'Price fell down!'
    body = f'Check the link : {url}'

    msg = f'Subject : {subject}\n\n {body}'

    server.sendmail(
        user_email,
        send_to_email,
        msg
    )
    
    print('Hey, email has been sent!')

    server.quit()

time_between_check = 43200

while True:
    check_price()
    sleep(time_between_check)