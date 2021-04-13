from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from crawler.models import CrawledPage


class HomeView(LoginRequiredMixin, View):

    def get(self, request):

        user = request.user

        pages = CrawledPage.objects.filter(user=user)
        context = {
            "pages": pages
        }

        return render(request=request, template_name='crawler.html', context=context)