from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import View


class MessagesView(LoginRequiredMixin, View):

    def get(self, request):
        context = {}

        return render(request, 'messages/list_messages.html', context=context)
