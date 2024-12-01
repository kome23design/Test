import requests
from bs4 import BeautifulSoup
import os
import csv


url="https://books.toscrape.com/"
page=requests.get(url)
x = BeautifulSoup(page.content, "html.parser")
if not os.path.exists("books"):
    os.mkdir("books")
list_books=["title","price","rate","image"]
y=x.find("h1").text.lower().replace(" ","_")
p=y+".csv"
G=x.find("ul", class_="nav")
a_elmt=G.find_all("a")

list_cont=[]
for i in a_elmt:
    li_elmt=i["href"]
    li_elmt=url+li_elmt
    list_cont.append(li_elmt)
list_cont.pop(0)

print(list_cont)

def to_get_all_the_infos_of_the_book():
    for i in list_cont:
        page=requests.get(i)
        k=BeautifulSoup(page.content, "html.parser")
        article_cont=k.find_all("article",class_="product_pod")
        L=k.find("h1").text.lower().replace(" ","_")
        N=L+".csv"
        print(N)
        list_category=[]
        with open("books/"+N, "w", encoding="utf-8-sig",newline="") as u:
            m=csv.writer(u)
            m.writerow(list_books)
            
            for p in article_cont:
                d=p.find("h3")
                d=d.find("a")
                list_file=[]
                list_file.append(d.string)
                price_tag=p.find("p",class_="price_color")
                list_file.append(price_tag.string)
                print(price_tag)
                rating=p.find("p",class_="star-rating")["class"]
                print(rating[1])
                rating = rating[1]
                if (rating=="five"):
                    rating=5
                elif (rating=="four"):
                    rating=4
                elif (rating=="three"):
                    rating=3
                elif (rating=="one"):
                    rating=1
                elif (rating=="two"):
                    rating=2
                list_file.append(rating)

                img_cont=p.find("img")
                src_cont=img_cont["src"]
                src_cont=url+src_cont
                src_cont=src_cont.replace("/../../../../", "/")
                list_file.append(src_cont) 

                """list_category.append(d)
                list_category.append(price_tag)"""

                m.writerow(list_file)
            
            #print(list_category)
to_get_all_the_infos_of_the_book()

