from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from django.shortcuts import redirect
from django.views.generic.base import View
from uploader.models.uploaded_file import UploadedFile

UPLOADED_FILE_ROOT = 'uploaded'


class UploadView(LoginRequiredMixin, View):

    def get(self, request):

        filepath = request.GET.get('filepath')
        filename = filepath.split('/')[-1]

        return FileResponse(open(filepath, "rb"), as_attachment=True, filename=filename)


    def post(self, request):
        user = request.user

        print(request.FILES)
        file = request.FILES.get('file')

        file_system_storage = FileSystemStorage()

        filename = "{}/{}/{}".format(UPLOADED_FILE_ROOT, user, file.name)

        upload_file = UploadedFile(path=filename, user=user)
        upload_file.save()

        file_system_storage.save(name=filename, content=file)

        return redirect(to='uploader:home')
