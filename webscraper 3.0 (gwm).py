#This program scrapes girlswithmuscle.com by input of the athlete's name. Then it retrieves the urls
#and then downloads the images/mp3s onto a folder

import bs4 as bs
import urllib.request
import os
import requests
import time
from page_loop import return_page_number



#naming here is sloppy, but is just to set to a stripped titlecase for ease of use/prevents errors
fbb_name = input('Enter fbb name: ')
fbb_name = fbb_name.title()
fbb_name = fbb_name.strip()

fbb_name_url = fbb_name.replace(' ','+')
folder_path = os.path.join(os.path.expanduser('~') , r'Pictures/Art Inspo/.muscles/Misc IRL', fbb_name)
image_log_path = os.path.join(folder_path,'.image_log.txt')


try:
    print(f'Creating new folder for {fbb_name}')
    os.makedirs(folder_path)
    with open(image_log_path, 'w'):
            pass

except FileExistsError:
    print('File folder Exists. Switching to update mode')
        
with open(image_log_path, 'r') as f:
    image_log = {line.strip() for line in f if line.strip()}


url = "https://www.girlswithmuscle.com/images/?name=" + fbb_name_url
page = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(page,'lxml')
number_of_pages = return_page_number(soup)

soups=[]
for i in range(1,number_of_pages+1):
    url_paginated = url.replace("images",f"images/{i}")
    page = urllib.request.urlopen(url_paginated).read()
    soups.append(bs.BeautifulSoup(page,'lxml'))





image_sources = [] #had to create an empty list for future conversion in order to remove ad/site images
for i in soups:
    for links in i.find_all('img'):
        image_source_raw = links.get("src")
        
        image_source_full = image_source_raw.replace('thumbs','full')
        image_sources.append(image_source_full)
        image_sources_cleaned = [k for k in image_sources if r'https://www.girlswithmuscle.com/images/' in k]



#loops through image_box and if there is a snag in the file type goes through try/except to get the right file type
#i know this part is really sloppy and can be cleaned up
#the x += 1 is solely for nomenclature to name the images/videos

image_sources_cleaned = set(image_sources_cleaned)
new_images = image_sources_cleaned - image_log

print('Retrieving ' + str(len(new_images)) + ' new images.')
x = 1
for items in new_images:
    image_name1 = fbb_name + ' (' + str(x) + ').jpg'
    image_name2 = fbb_name + ' (' + str(x) + ').mp4'
    image_name3 = fbb_name + ' (' + str(x) + ').png'
    
    try:
        try:
            urllib.request.urlretrieve(items, os.path.join(folder_path, image_name1))
            x += 1 
        except:
            items = items.replace('jpg','mp4')
            urllib.request.urlretrieve(items, os.path.join(folder_path, image_name2))
            x += 1
    except:
        items = items.replace('mp4','png')
        urllib.request.urlretrieve(items, os.path.join(folder_path, image_name3))
        x += 1


with open(image_log_path, 'a') as f:
    for item in new_images:  # Changed 'set' to 'my_set'
        f.write(f"{item}\n")
    
print('Done.')
    







    
    

    


