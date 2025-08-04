from django.shortcuts import render

# Create your views here.


def NewsHome(request):
    return render(request, 'MySiteApp/index.html')