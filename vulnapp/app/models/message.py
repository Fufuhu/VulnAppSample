from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin


class Message(models.Model):

    class Meta:
        db_table = 'messages'

    body = models.TextField(verbose_name='本文')
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'body', 'created_at', 'created_at', 'updated_at')