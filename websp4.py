import requests
from bs4 import BeautifulSoup
import os

url="http://books.toscrape.com/catalogue/rip-it-up-and-start-again_986/index.html"
page = requests.get(url)
x = BeautifulSoup(page.content, "html.parser")
if not os.path.exists("pictures"):
    os.mkdir("pictures")
h = x.find_all("img")
for i in h:
    f=i["src"]
    f=f.replace("../..", "http://books.toscrape.com")
    t=i["alt"]
    with open("pictures/"+t+".jpg", "wb") as k:
        c=requests.get(f)
        k.write(c.content)



