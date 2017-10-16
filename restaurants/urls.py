from django.conf.urls import url
from restaurants.views import *
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^restaurants/$', restaurant_list),
    
]