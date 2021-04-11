from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import View

from uploader.models import UploadedFile


class HomeView(LoginRequiredMixin, View):

    def get(self, request):
        context = {}

        uploaded_files = UploadedFile.objects.filter(user=request.user)

        context['uploaded_files'] = uploaded_files

        return render(request=request, template_name='uploader.html',context=context)
