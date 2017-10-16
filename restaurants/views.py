from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .models import *

# Create your views here.
def restaurant_list(request):
	template_name = 'restaurants/restaurants_list.html'
	queryset = Restaurant.objects.all()
	context = {
		'object_list': queryset
	}
	return render(request, template_name, context)
