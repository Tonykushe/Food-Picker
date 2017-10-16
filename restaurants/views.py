from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import *

# Create your views here.
def restaurant_list(request):
	template_name = 'restaurants/restaurants_list.html'
	queryset = Restaurant.objects.all()
	context = {
		'object_list': queryset
	}
	return render(request, template_name, context)

class RestaurantListView(ListView):
	def get_queryset(self):
		slug = self.kwargs.get('slug')
		if slug:
			queryset = Restaurant.objects.filter(
					Q(category__iexact=slug) |
					Q(category__icontains=slug)
				)
		else:
			queryset = Restaurant.objects.all()

		return queryset

class RestaurantDetailView(DetailView):
	queryset = Restaurant.objects.all()


