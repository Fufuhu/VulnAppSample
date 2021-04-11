from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import View

from app.models.message import Message


class MessagesView(LoginRequiredMixin, View):

    def get(self, request):
        context = {}

        user = request.user
        context['messages'] = Message.objects.filter(user=user)

        return render(request, 'messages/list_messages.html', context=context)

    def post(self, request):
        context={}

        user = request.user
        body = request.POST.get('body')
        print(body)

        message = Message(body=body, user=user)
        message.save()

        context['messages'] = Message.objects.filter(user=user)

        return render(request, 'messages/list_messages.html', context=context)
