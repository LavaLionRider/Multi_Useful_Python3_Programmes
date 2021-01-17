import requests
import time
from PIL import Image  
import io
from datetime import datetime

def download(i):
    
    img = requests.get('https://thispersondoesnotexist.com/image', headers={'User-Agent': 'My User Agent 1.0'}, stream=True).raw
    im = Image.open(img)
    newsize = (60, 60) #give the size of the you want. you can also ignore and remove it and next line
    im1 = im.resize(newsize)
    im1.save('images/img '+str(i)+'.jpg') #saving the photo to the address
    
s = time.time()

for i in range(11): #how many photos you need it counts from 0 to...
    time.sleep(1.5) #sleep time for refreshing the site to avoid saveing same photo 1.5 is good.
    download(i)
f = time.time() #It gives you the time for processing in Second

print(str(f-s) + " Second")

