from django.conf.urls import url
from restaurants.views import *
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

urlpatterns = [
	url(r'^login/$', LoginView.as_view(), name='login'),
	url(r'^restaurants/$', RestaurantListView.as_view(), name='restaurants'),
	url(r'^restaurants/create/$', RestaurantCreateView.as_view(), name='restaurants-create'),
    url(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='restaurants-detail'),

    #url(r'^restaurants/(?P<slug>\w+)/$', RestaurantListView.as_view()),
    # url(r'^restaurants/african/$', AfricanRestaurantListView.as_view()),
    # url(r'^restaurants/brazillian/$', BrazillianRestaurantListView.as_view()),

    
]