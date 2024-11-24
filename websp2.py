import requests
from bs4 import BeautifulSoup
import os


url="http://books.toscrape.com/catalogue/sophies-world_966/index.html"
page = requests.get(url) #to recover all the contents of the page
x = BeautifulSoup(page.content, "html.parser") #to annylyse the content
if not os.path.exists("image"): #to create a folder of image
    os.mkdir("image")
y_img = x.find_all("img")
listm =[]
for i in y_img:
    listm.append(i.string)
    k=i["src"] #scr to get just the image not with the properties Alt
    k=k.replace("../..", "http://books.toscrape.com")
    d=i["alt"]
    with open("image/"+d+".jpg","wb") as u:
         z=requests.get(k)
         u.write(z.content)
   
print(listm)
