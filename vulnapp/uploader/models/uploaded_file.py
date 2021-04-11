from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models


class UploadedFile(models.Model):
    class Meta:
        db_table = 'uploaded_files'

    path = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'path', 'created_at', 'updated_at', 'user')
