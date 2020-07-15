# PriceWatch
Monitors the price of a product you want, and sends an email alert when the price drops below your budget. The program uses BeautifulSoup4 to parse the HTML and smtplib to send emails.

# Running the Program
You'll need to install BeautifulSoup4. To receive the email alerts, set up 2 Factor Authentication, and generate an app password for mail on your device. Find the ids of the tags in which the product title and product price are located. To find out your User Agent, search "my user agent" and copy the information in the box into the dictionary named "header". 

The program waits 12 hours before checking the price again. This value can be modified by changing the "time_between_check" variable. To exit the prorgram, use the keyboard interrupt (CTRL + C).

Note: This may not work on all websites, as some websites do not allow webscraping.
