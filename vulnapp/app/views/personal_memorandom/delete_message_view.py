from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic.base import View

from app.models import Message


class DeleteMessageView(LoginRequiredMixin, View):

    def get(self, request, message_id):

        user = request.user

        Message.objects.filter(user=user, id=message_id).delete()
        return redirect(to='messages')