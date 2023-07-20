from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('items/', list, name='list'),
    path('plus_id/', plus_id, name='plus_id')
]
