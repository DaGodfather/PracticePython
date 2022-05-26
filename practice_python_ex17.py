#! python 3
# Decode a webpage

import requests
from bs4 import BeautifulSoup
import lxml

nyURL = "https://www.nytimes.com"
request = requests.get(nyURL)

#Put resonse into html string
request_html = request.text

#use BeautifilSoup to parse the HTML
soup = BeautifulSoup(request_html, features= "lxml")

#find all H3 tags which appear to be titles of articles into a list
headerTitle = soup.find_all('h3') 

#get the string(article title) for each element in the list
for item in headerTitle:
    print(item.string + "\n")



