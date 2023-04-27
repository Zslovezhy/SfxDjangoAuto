# _*_ coding: utf-8 _*_
"""
Time:     2023/4/26 16:27
Author:   Sen Zhang
File:     urls.py
Version:  V1.0  2023/4/26 16:27
Describe: 
Steps:
    1.
    2.
    ...
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'uploadlog/', uploadLog),
]