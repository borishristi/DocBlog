from django.shortcuts import render
from datetime import datetime


def index(requests):

    date = datetime.today()
    print(date)
    print(type(date))
    return render(requests, "DocBlog/index.html", context={"date": datetime.today()})