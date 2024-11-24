import requests
from bs4 import BeautifulSoup
import os

url="http://books.toscrape.com/catalogue/sharp-objects_997/index.html"
page = requests.get(url)
t = BeautifulSoup(page.content, "html.parser")
if not os.path.exists("photos"):
    os.mkdir("photos")
qp = t.find_all("img")
listB =[]
for i in qp:
    listB.append(i)
    w=i["src"]
    w=w.replace("../..", "http://books.toscrape.com")
    h=i["alt"]
    with open("photos/"+h+".jpg", "wb") as y:
        n=requests.get(w)
        y.write(n.content)
    

print(listB)

