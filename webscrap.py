import requests #to handle the request of http
from bs4 import BeautifulSoup #to annalyse the response of request
import os #gives permission to create a folder
import csv


url="http://books.toscrape.com/catalogue/sophies-world_966/index.html"
page = requests.get(url) #to recover all the contents of the page
x = BeautifulSoup(page.content, "html.parser") #to annylyse the content
if not os.path.exists("image"): #to create a folder of image
    os.mkdir("image") #command to create a file
if not os.path.exists("data"):
    os.mkdir("data")

p_content = x.find_all("p")
list_title =["title"]
y_img = x.find("img")
k=y_img["src"] #scr to get just the image not with the properties Alt
k=k.replace("../..", "http://books.toscrape.com")
d=y_img["alt"]
with open("image/"+d+".jpg","wb") as u:
    z=requests.get(k)
    u.write(z.content) #to copy the images in the file
a_cont = x.find_all("a")
print(a_cont)
listp  =[] #looping over the p content
for i in p_content:
    listp.append(i.string)
print(listp)

p = x.find("h1").text.lower().replace(" ","_") #we recover the h1 of the page putting them in lower case letters and replacing the spacing with underscourt
file_name=p+".csv" #csv file created and named after the h1 of the page recovered
all_h3=x.find_all("h3") 
with open("data/"+file_name, "w",encoding="utf-8-sig",newline="") as b: 
    csv_file = csv.writer(b)
    csv_file.writerow(list_title)
    for i in all_h3:
        a_content = i.find("a")
        csv_file.writerow(a_content.string)
