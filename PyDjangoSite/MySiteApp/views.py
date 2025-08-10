from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(response):
    return render(response,'MySiteApp/index.html')
def info(response):
    return render(response,'MySiteApp/info.html')

