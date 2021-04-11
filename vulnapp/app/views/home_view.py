from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import View



class HomeView(LoginRequiredMixin, View):

    def get(self, request):
        context = {}
        return render(request=request,
                      template_name='home.html',
                      context=context)
