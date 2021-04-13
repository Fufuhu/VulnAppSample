from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models


class CrawledPage(models.Model):
    class Meta:
        db_table = 'crawled_pages'

    url = models.CharField(verbose_name='URL', max_length=255, blank=False)
    memo = models.CharField(verbose_name='メモ', max_length=255, null=True)
    content = models.TextField(verbose_name='コンテンツ')
    created_at = models.DateTimeField(verbose_name='クロール日時', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


@admin.register(CrawledPage)
class CrawledPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'created_at')
