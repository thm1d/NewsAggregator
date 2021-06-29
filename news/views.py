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


def index(req):
    return render(req, 'news/index.html', {'tbt_news':tbt_news, 'ds_news': ds_news})