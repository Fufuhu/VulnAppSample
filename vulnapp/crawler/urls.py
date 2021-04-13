from django.urls import path

from crawler.views.home_view import HomeView

app_name = 'crawler'

urlpatterns = [
    path('', HomeView.as_view(), name='home')
]