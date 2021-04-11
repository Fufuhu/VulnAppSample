from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):

    class Meta:
        db_table = 'messages'

    body = models.TextField(verbose_name='本文')
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_ad = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    user = models.ForeignKey(User)
