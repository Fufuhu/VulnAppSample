from django.shortcuts import render
from django.views.generic.base import View


class MessageView(View):

    def get(self, request):
        context = {}

        return render(request, 'messages/post_message.html', context=context)
