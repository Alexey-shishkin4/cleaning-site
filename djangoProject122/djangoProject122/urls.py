from django.contrib import admin
from django.urls import path

from bboard.views import bb_index
from index.views import index
from orders.views import success


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('order/', bb_index),
    path('success/', success, name='success'),
]
