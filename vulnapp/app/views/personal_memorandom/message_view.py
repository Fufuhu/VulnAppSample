from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import View

from app.models.message import Message


class MessageView(LoginRequiredMixin, View):

    def get(self, request):
        context = {}

        return render(request, 'messages/post_message.html', context=context)

    def post(self, request):
        context={}

        user = request.user
        body = request.POST.get('body')
        print(body)

        message = Message(body=body, user=user)
        message.save()

        return render(request, 'messages/list_messages.html', context=context)
