from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.
def home(request):
    return render (request, 'index.html')

def category(request, cat_id):
    return HttpResponse(f"<h1>(cat_id)</h1>")  

def archive(request,year):
    return HttpResponse(f"<h1>{year}</h1>")  

def customhandler404(request):
    response = render(request, '404.html',)
    response.status_code = 404
    return response