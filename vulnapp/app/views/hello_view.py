from django.http import HttpResponse

# Create your views here.

def hello(req):
    return HttpResponse('Hello world! Django.')