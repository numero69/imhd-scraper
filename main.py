from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
from datetime import datetime

city_code = input("input city code: ")
myurl = "https://imhd.sk/" + city_code + "/informacie"

f = open("imhd_" + city_code + ".csv", "w", encoding="utf-8-sig")
headers = "Category, Title, Posted on"
f.write(headers + "\n")

uClient = ureq(myurl)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

#container (grab all news)
row = page_soup.findAll("div", {"class":"Card-body"})

for novinka in row:
    title = novinka.h2.a.text
    category = novinka.a.text
    date = novinka.time
    date_text = date["datetime"]
    date_clear = date_text.replace("-", "/")
    date_clear = date_clear[:-15]
    date_object = datetime.strptime(date_clear, '%Y/%m/%d')
    date_print = date_object.strftime('%d %m %Y')
    print("----------------")
    print("["+category+"]")
    print(title)
    print(date_print)
    f.write((category + "," + title.replace(",", " ") + "," + date_clear + "\n"))
f.close()