
from django.contrib import admin
from django.urls import path, include
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('items/', list),
    path('plus_id/', plus_id)
]