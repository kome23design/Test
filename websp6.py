import requests
from bs4 import BeautifulSoup
import os
import csv


url="https://books.toscrape.com/"
page=requests.get(url)
x = BeautifulSoup(page.content, "html.parser")
if not os.path.exists("books"):
    os.mkdir("books")
list_books=["title"]
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
        h3_cont=k.find_all("h3")
        L=k.find("h1").text.lower().replace(" ","_")
        N=L+".csv"
        print(N)
        list_category=[]
        with open("books/"+N, "w", encoding="utf-8-sig",newline="") as u:
            m=csv.writer(u)
            m.writerow(list_books)
            
            for p in h3_cont:
                d=p.find("a")
                m.writerow(d)
                m.writerow(list_books)

                list_category.append(d)

                
            
            #print(list_category)
to_get_all_the_infos_of_the_book()



   
    


