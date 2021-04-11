from django.urls import path

from uploader.views.home_view import HomeView

app_name = 'uploader'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]