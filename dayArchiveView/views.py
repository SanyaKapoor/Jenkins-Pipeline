from django.shortcuts import render

from django.views.generic.dates import DayArchiveView

from list.models import Article

class ArticleDayArchiveView(DayArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    allow_future = True