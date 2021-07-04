from django.shortcuts import render

def newsList(req):
    return render(req, 'sources/sources.html')