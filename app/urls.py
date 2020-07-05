"""MyNovel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from MyNovel import settings
from app import views

urlpatterns = [
    re_path(r'index/(?P<page_num>\d+)$',views.indexPage,name='index'),
    path('test/',views.testT),
    re_path('chapter/(?P<book_id>\d+)$',views.novleChapters,name='chapter'),
    re_path(r'content/(?P<book_id>\d+)/(?P<chapter_num>\d+)$',views.novelContent,name='content'),
    path('search/',views.searchNovel,name='search'),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
]
