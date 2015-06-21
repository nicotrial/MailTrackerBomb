__author__ = 'Nicotrial'

#MailTrackerBomb is a small gag tool to anoy people with Mailtracker sending many requests to the tracker image
#in the email url.. and having the mailtracke notification pop up all day long.. Have fun..

import requests
import sys
import time

print("Insert url of mailtracker png from mail source code")
url = input("Enter url: ")
print("Number of email reads to send")
max_pages = int(sys.stdin.readline())
print("delay in seconds between requests (if too fast not all request go through 0.3 is good the slower the more anoying)")
delay = float(sys.stdin.readline())
print(url)
print(max_pages)
page = 0

while page <= max_pages:
    requests.get(url).content
    print("Sent")
    page = page + 1
    time.sleep(delay)
print("done!!lol")
