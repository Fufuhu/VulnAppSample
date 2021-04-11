from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.base import View

from django.db import connection

from app.models import Message


class MessageView(LoginRequiredMixin, View):

    def get(self, request, message_id=None):
        context = {}

        mid = request.GET.get('message_id')
        if mid:
            with connection.cursor() as cursor:
                sql ="""
                    SELECT "messages"."id", "messages"."body", "messages"."created_at", "messages"."updated_at", "messages"."user_id" FROM "messages" WHERE "messages"."id" = {};
                """.format(mid,mid)
                # print(sql)
                c = cursor.executescript(sql)
                result = c.fetchall()
                # print(result)
            return redirect(to='search_message', message_id=mid)

        if message_id is not None:
            message = Message.objects.get(id=message_id)
            context['message'] = message

            return render(request, 'messages/search_message.html', context=context)

        return render(request, 'messages/search_message.html', context=context)

