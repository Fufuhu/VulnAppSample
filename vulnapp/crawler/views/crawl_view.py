from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic.base import View
import requests

from crawler.models import CrawledPage


class CrawlView(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user
        url = request.GET.get('url')
        memo = request.GET.get('memo')
        r = requests.get(url)
        content = r.text[0:255]

        page = CrawledPage(url=url, content=content, memo=memo, user=user)
        page.save()

        return redirect(to='crawler:home')
