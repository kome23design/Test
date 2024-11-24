import requests
from bs4 import BeautifulSoup
import os
import csv

url="http://books.toscrape.com/catalogue/without-borders-wanderlove-1_956/index.html"
page = requests.get(url)
x = BeautifulSoup(page.content, "html.parser")
if not os.path.exists("info"):
    os.mkdir("info")
list_title=["title","price","rate"] #to get both the title and prices
y = x.find("h1").text.lower().replace(" ","_")
f_name=y+".csv"
h3_cont=x.find_all("article",class_="product_pod") #so we include the main tag and the class tag for the title
with open("info/"+f_name, "w", encoding="utf-8-sig",newline="") as u:
    v=csv.writer(u)
    v.writerow(list_title)
    for i in h3_cont:
        h_element=i.find("h3")
        a_cont=h_element.find("a")
        price_tag=i.find("p",class_="price_color") #the tag and the class tag for prices
        rating=i.find("p",class_="star-rating")    
        list_cont=[] #add to the list
        list_cont.append(a_cont.string) #we string so as to not include both the tag and title
        list_cont.append(price_tag.string) #string so as to not include both tag and price
        list_cont.append(rating.string)
        if (rating=="five"):
            print("five stars")
        elif (rating=="four"):
            print("four stars")
        elif (rating=="two"):
            print("two stars")
        elif (rating=="one"):
            print("one star")

        v.writerow(list_cont)