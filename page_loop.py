import bs4 as bs
import urllib.request
import os
import requests
import time

fbb_name = "Meghan Morrison (Santa Barbara)"
fbb_name = fbb_name.title()
fbb_name = fbb_name.strip()

fbb_name_url = fbb_name.replace(' ','+')

url = "https://www.girlswithmuscle.com/images/?name=" + fbb_name_url
page = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(page,'lxml')
x = 0

def return_page_number(soup):
    # 1. Find the "next" button
    next_button = soup.find('a', class_='paginator-next')

    # 2. Get the text immediately before it
    # .previous_sibling captures the " Page 1 of 8 " text node
    pagination_text = next_button.previous_sibling.strip()

    # 3. Extract the last number
    # Split the string ["Page", "1", "of", "8"] and take the last element
    total_pages = int(pagination_text.split()[-1])

    return total_pages


print(return_page_number(soup))