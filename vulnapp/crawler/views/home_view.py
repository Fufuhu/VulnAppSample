from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View


class HomeView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request=request, template_name='crawler.html', context={})