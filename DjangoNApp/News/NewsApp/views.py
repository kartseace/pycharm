from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.

def Index(request):
    newsapi = NewsApiClient(api_key="f6301f1d41c447398c1b3ca11a7c7ba4")
    topheadlines = newsapi.get_top_headlines(sources='al-jazeera-english',
                                          )
    articles=topheadlines['articles']
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles=articles[i]

        news.append(myarticles['title'])

        desc.append(myarticles['description'])

        img.append(myarticles['urlToImage'])

    mylist = zip(news,desc,img)
    return render(request,'index.html',context={"mylist":mylist})

def bbc(request):
    newsapi = NewsApiClient(api_key="f6301f1d41c447398c1b3ca11a7c7ba4")
    topheadlines = newsapi.get_top_headlines(sources='bbc-news',
                                          )
    articles=topheadlines['articles']
    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles=articles[i]

        news.append(myarticles['title'])

        desc.append(myarticles['description'])

        img.append(myarticles['urlToImage'])

    mylist = zip(news,desc,img)
    return render(request,'bbc.html',context={"mylist":mylist})