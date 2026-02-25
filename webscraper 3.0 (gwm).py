#This program scrapes girlswithmuscle.com by input of the athlete's name. Then it retrieves the urls
#and then downloads the images/mp3s onto a folder

import bs4 as bs
import urllib.request
import os
import requests
import time

pre_image_box = [] #had to create an empty list for future conversion in order to remove ad/site images

#naming here is sloppy, but is just to set to a stripped titlecase for ease of use/prevents errors
fbb_name = input('Enter fbb name: ')
fbb_name = fbb_name.title()
fbb_name = fbb_name.strip()

fbb_name_url = fbb_name.replace(' ','+')


my_path = '/home/andy/Pictures/' + fbb_name
new_path = my_path + ' (new)'
try:
    os.makedirs(my_path)
except:
    print('There is already a folder named ' + fbb_name)
    input('Do you want to make a new folder? Press enter to continue: ')
    os.makedirs(new_path)
        

#user input

url = "https://www.girlswithmuscle.com/images/?name=" + fbb_name_url
page = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(page,'lxml')
x = 0


#print(soup.prettify())
#print(len(soup.find_all('img'))) #finds images

#this block is for getting the urls and putting them into a filtered list 'image_box'

print('Acquiring urls...')
for links in soup.find_all('img'):
    image_source = links.get("src")
    
    image_source2 = image_source.replace('thumbs','full')
    pre_image_box.append(image_source2)
    image_box = [k for k in pre_image_box if r'https://www.girlswithmuscle.com/images/' in k]
print('Done acquiring urls.')

#loops through image_box and if there is a snag in the file type goes through try/except to get the right file type
#i know this part is really sloppy and can be cleaned up
#the x += 1 is solely for nomenclature to name the images/videos

print('Retrieving top images and videos...')
for items in image_box:
    image_name1 = fbb_name + ' (' + str(x) + ').jpg'
    image_name2 = fbb_name + ' (' + str(x) + ').mp4'
    image_name3 = fbb_name + ' (' + str(x) + ').png'
    
    try:
        try:
            urllib.request.urlretrieve(items, os.path.join(my_path, image_name1))
            x += 1 
        except:
            items = items.replace('jpg','mp4')
            urllib.request.urlretrieve(items, os.path.join(my_path, image_name2))
            x += 1
    except:
        items = items.replace('mp4','png')
        urllib.request.urlretrieve(items, os.path.join(my_path, image_name3))
        x += 1

    
    
print('Done.')
    







    
    

    


