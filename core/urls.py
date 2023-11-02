from django.urls import path
from django.urls import re_path
from .views import *
urlpatterns = [
    path('', home , name='home'),
    path('page/<slug:cat_id>/', category, name='category'),
    re_path(r"^archive/,(?P<year>[0-9]{4})/",archive),
    path('', customhandler404 , name='404')
]