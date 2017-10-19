from django.conf.urls import url
from restaurants.views import *
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^restaurants/$', RestaurantListView.as_view()),
    url(r'^restaurants/(?P<rest_id>\w+)/$', RestaurantDetailView.as_view()),

    #url(r'^restaurants/(?P<slug>\w+)/$', RestaurantListView.as_view()),
    # url(r'^restaurants/african/$', AfricanRestaurantListView.as_view()),
    # url(r'^restaurants/brazillian/$', BrazillianRestaurantListView.as_view()),

    
]