import requests #to handle the request of http
from bs4 import BeautifulSoup #to annalyse the response of request
import os #gives permission to create a folder


url="http://books.toscrape.com/catalogue/sophies-world_966/index.html"
page = requests.get(url) #to recover all the contents of the page
x = BeautifulSoup(page.content, "html.parser") #to annylyse the content
if not os.path.exists("image"): #to create a folder of image
    os.mkdir("image") #command to create a file
p_content = x.find_all("p")
y_img = x.find("img")
k=y_img["src"] #scr to get just the image not with the properties Alt
k=k.replace("../..", "http://books.toscrape.com")
d=y_img["alt"]
with open("image/"+d+".jpg","wb") as u:
    z=requests.get(k)
    u.write(z.content)
a_cont = x.find_all("a")
print(a_cont)
listp  =[] #looping over the p content
for i in p_content:
    listp.append(i.string)
print(listp)