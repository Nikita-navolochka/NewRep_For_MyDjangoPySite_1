from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static #31.07.25 append for css for <<settings.py>>

urlpatterns = [

    path('', views.index, name="home"), #01.08.25 append name
    path('info', views.info, name = "info"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #31.07.25 append for css for <<settings.py>>