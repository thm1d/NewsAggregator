from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from .forms import SelectForm



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

tna_r = requests.get("https://www.newagebd.net/articlelist/302/Bangladesh")
tna_soup = BeautifulSoup(tna_r.content, 'html.parser')
tna_headings = tna_soup.find_all('h3')
tna_headings = tna_headings[1:-1]
tna_news = []

for tna in tna_headings:
    tna_news.append(tna.text)

#Getting news The Daily Observer

tdo_r = requests.get("https://www.observerbd.com/cat.php?cd=186")
tdo_soup = BeautifulSoup(tdo_r.content, 'html.parser')
tdo_headings = tdo_soup.find_all('b')
tdo_news = []

for tdo in tdo_headings:
    tdo_news.append(tdo.text)

#Getting news BDNews24

bd_r = requests.get("https://bdnews24.com/bangladesh/")
bd_soup = BeautifulSoup(bd_r.content, 'html.parser')
bd_headings = bd_soup.find_all('h6')
bd_news = []

for bd in bd_headings:
    bd_news.append(bd.text)

#Getting news Dhaka Tribune

dt_r = requests.get("https://www.dhakatribune.com/articles/bangladesh")
dt_soup = BeautifulSoup(dt_r.content, 'html.parser')
dt_headings = dt_soup.find_all("h4", {"class": "news-title"})
dt_news = []

for dt in dt_headings:
    dt_news.append(dt.text)

def aggregate(req):
    source_one = ''
    source_two = ''
    if req.method == 'POST':
        form = SelectForm(req.POST)
        if form.is_valid():

            source_one = form.cleaned_data['select_source_one']
            source_two = form.cleaned_data['select_source_two']

    form = SelectForm()
    return render(req, 'news/aggregate.html', {'source_one': source_one, 'source_two': source_two, 'tdo_news': tdo_news, 'dt_news': dt_news, 'bd_news': bd_news, 'tbt_news':tbt_news, 'tds_news': ds_news, 'tna_news': tna_news, 'form': form})

def index(req):
    return render(req, 'news/index.html')