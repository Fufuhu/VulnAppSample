from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic.base import View


class HomeView(LoginRequiredMixin, View):

    def get(self, request):
        return HttpResponse('Hello world! Django.')
