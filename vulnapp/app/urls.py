from django.urls import path, re_path
from .views.home_view import HomeView
from .views.personal_memorandom.message_view import MessageView
from .views.personal_memorandom.messages_view import MessagesView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('message/', MessageView.as_view(), name='message'),
    path('message/<int:message_id>/', MessageView.as_view(), name='search_message'),
    path('messages/', MessagesView.as_view(), name='messages'),
]
