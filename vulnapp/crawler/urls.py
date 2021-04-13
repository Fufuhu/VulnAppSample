from django.urls import path

from crawler.views.crawl_view import CrawlView
from crawler.views.home_view import HomeView

app_name = 'crawler'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('crawl/', CrawlView.as_view(), name='crawl')
]