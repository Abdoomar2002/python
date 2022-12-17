import csv
import requests
import bs4

rows=[]
a=[]
## الكود بيطول في التشغيل فجرب علي صفحات قليلة في اللوب
for i in range(1,43,1):
    url = "https://www.wifi4games.com/pc_games/" + str(i) + "/index.html"
    page = requests.get(url)
    page = bs4.BeautifulSoup(page.content, "html.parser")
    a = page.find_all("a", {"id": "TheNameOfApp"})
    for j in a:
        subUrl = "https://www.wifi4games.com" + j.get('href')
        subpage = requests.get(subUrl)
        subpage = bs4.BeautifulSoup(subpage.content, "html.parser")
        div = subpage.find_all("div", {"class": "light"})
        rate = div[0].find("span", {"class": "icon"})
        rate = str(rate.get('data-stars'))
        download = div[0].find("span", {"style": "padding:0 8px;border-left:1px solid;border-right:1px solid;"})
        download = str(download.get_text())
        views = div[0].find_all("span", {"style": "padding:0 8px;"})
        views = str(views[len(views) - 1].get_text())
        div = subpage.find_all("div", {"style": "word-wrap: break-word;"})
        story = str(div[0].get_text())
        name = j.find("span", {"class": "strong"})
        name=str(name.get_text())
        size = j.find("span", {"class": "light"})
        size=str(size.get_text())
        rows.insert(len(rows),[a.index(j)+1,name,size,rate,download,views,story])


filename = "Games.text"

# writing to csv file
with open(filename, 'w',encoding="utf-16") as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the data rows
    csvwriter.writerows(rows)


