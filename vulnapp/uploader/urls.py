from django.urls import path

from uploader.views.home_view import HomeView
from uploader.views.upload_view import UploadView

app_name = 'uploader'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('upload/', UploadView.as_view(), name='upload')
]