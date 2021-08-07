from django.shortcuts import render,HttpResponse
import requests

# def index(request):
#     return render(request,"home\index.html")
def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')
