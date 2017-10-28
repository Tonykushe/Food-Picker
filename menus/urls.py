from django.conf.urls import url
from menus.views import *


urlpatterns = [
	url(r'^$', ItemListView.as_view(), name='list'),
	url(r'^create/$', ItemCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', ItemDetailView.as_view(), name='detail'),

]