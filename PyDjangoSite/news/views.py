from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
# Create your views here.

def NewsHome(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news.html', {'news':news})


def CreateNews(request):
    error=''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(' http://127.0.0.1:8000/')
        else:
            error = 'error'


    form = ArticlesForm()

    data = {
        'form': form,
        'error':error
    }
    return render(request, 'news/CreateNews.html', data)

