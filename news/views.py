from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# GEtting news from The Bangladesh Today

tbt_r = requests.get("https://thebangladeshtoday.com/?cat=8")
tbt_soup = BeautifulSoup(tbt_r.content, 'html.parser')

tbt_headings = tbt_soup.find_all('h3')

tbt_headings = tbt_headings[:] # removing footers

tbt_news = []

for tbt in tbt_headings:
    tbt_news.append(tbt.text)



#Getting news The Daily Star

ds_r = requests.get("https://www.thedailystar.net/todays-news")
ds_soup = BeautifulSoup(ds_r.content, 'html.parser')
ds_headings = ds_soup.find_all("td", {"class": "views-field-title"})
ds_headings = ds_headings[:15]
ds_news = []

for ds in ds_headings:
    ds_news.append(ds.text)

#Getting news The New Age

na_r = requests.get("https://www.newagebd.net/articlelist/302/Bangladesh")
na_soup = BeautifulSoup(na_r.content, 'html.parser')
na_headings = na_soup.find_all('h3')
na_headings = na_headings[1:-1]
na_news = []

for na in na_headings:
    na_news.append(na.text)


def aggregate(req):
    return render(req, 'news/aggregate.html', {'tbt_news':tbt_news, 'ds_news': ds_news, 'na_news': na_news})

def index(req):
    return render(req, 'news/index.html')