from django.shortcuts import render
from .models import Articles
# Create your views here.

news = Articles.objects.all()
def NewsHome(request):
    return render(request, 'news/news.html', {'news':news})