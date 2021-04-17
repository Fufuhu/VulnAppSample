from django.urls import path, re_path
from .views.home_view import HomeView
from .views.personal_memorandom.delete_message_view import DeleteMessageView
from .views.personal_memorandom.message_view import MessageView
from .views.personal_memorandom.messages_view import MessagesView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('message/', MessageView.as_view(), name='message'),
    path('message/<int:message_id>/', MessageView.as_view(), name='search_message'),
    path('message/<int:message_id>/delete', DeleteMessageView.as_view(), name='delete_message'),
    path('messages/', MessagesView.as_view(), name='messages'),
]
